from flask import Flask
from flask_sqlalchemy import SQLAlchemy

file_name = "db.house"

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# try:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123321@192.168.1.4:5432/first_db'
#     print("Connected to PostgreSQL")
#     db = SQLAlchemy(app)
# except:
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.house'
#     print("PostgreSQL is not available - Connected to Sqlite3")
#     db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + file_name
print("PostgreSQL is not available - Connected to Sqlite3")
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "AVec8KV4tLq5!V!@L?p7BW%j+8E$E2k-x2Zg-+kajHqg?XxV"
