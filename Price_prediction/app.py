from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask.helpers import url_for
from house_analyze import convert_for_prediction, make_reshape, round_1000_down, round_1000_up, list_to_dict
from house_analyze import model
from appconfig import app, db, file_name
from flask_db import House, User2
from flask_db import create_db


login_manager = LoginManager()
login_manager.init_app(app)


create_db(file_name)


@login_manager.user_loader
def load_user(user_id):

    return User2.query.get(user_id) 


@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")


@app.route("/calculate", methods=['GET', 'POST'])
@login_required
def calculate():
    result_down = None
    result_up = None
    bedrooms = (request.form.get("bedrooms", None))
    bathrooms = (request.form.get("bathrooms", None))
    sqft_living = (request.form.get("sqft_living", None))
    sqft_lot = (request.form.get("sqft_lot", None))
    floors = (request.form.get("floors", None))
    condition = (request.form.get("condition", None))
    sqft_above = (request.form.get("sqft_above", None))
    sqft_basement = (request.form.get("sqft_basement", None))
    years_old = (request.form.get("years_old", None))
    city = (request.form.get("city", None))

    if sqft_above and sqft_living and sqft_basement and sqft_lot and years_old:

        x_test = convert_for_prediction(bedrooms, bathrooms, sqft_living, sqft_lot,
                                        floors, condition, sqft_above, sqft_basement, years_old, city)

        x_test = make_reshape(x_test)
        result = model.predict(x_test)
        result_up = round_1000_up(result)
        result_down = round_1000_down(result)

        house = House(bedrooms=bedrooms, bathrooms=bathrooms, sqft_living=sqft_living, sqft_lot=sqft_lot, floors=floors,
                      condition=condition, sqft_above=sqft_above, sqft_basement=sqft_basement, years_old=years_old, city=city, prize=result)
        db.session.add(house)
        db.session.commit()

    return render_template("calculate.html", result_up=result_up, result_down=result_down)


@app.route("/register", methods=["GET", "POST"])
def register():
    username = (request.form.get("username", None))
    email = (request.form.get("email", None))
    password = (request.form.get("password", None))
    print("working")

    if username and email and password:
        user1 = User2(username=username, email=email, password=password)
        db.session.add(user1)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        return render_template("register.html", username=username)



@app.route("/login", methods=["GET", "POST"])
def login():
    username = (request.form.get("username", None))
    password = (request.form.get("password", None))

    if username and password:
        user1 = User2.query.filter_by(
            username=username).filter_by(password=password).first()
        if user1:
            print("__________ user found.")
            login_user(user1)
            return redirect(url_for("calculate"))

        else:
            print("__________ user not found.")

    return render_template("login.html", username=username)



@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))






@app.route("/api/house/", methods=["POST"])
def house_api():

    if request.json:
        data = request.json
        print(data)
        bedrooms = data["bedrooms"]
        bathrooms = data["bathrooms"]
        sqft_living = data["sqft_living"]
        sqft_lot = data["sqft_lot"]
        floors = data["floors"]
        condition = data["condition"]
        sqft_above = data["sqft_above"]
        sqft_basement = data["sqft_basement"]
        years_old = data["years_old"]
        city = data["city"]

        x_test = convert_for_prediction(bedrooms, bathrooms, sqft_living, sqft_lot,
                                        floors, condition, sqft_above, sqft_basement, years_old, city)

        x_test = make_reshape(x_test)
        result = model.predict(x_test)
        result = round_1000_down(result)

        return {"calculated value": result}
    else:

        return {"ERROR": "JSON expected"}


@app.route("/api/house/<int:Id>")
def api_price(Id):
    Id = (Id % 10) + 1
    result = db.session.execute(f"SELECT * FROM House where Id = {Id}")

    for value in result:
        val = value

    house_dict = list_to_dict(val)
    return house_dict






