import numpy as np
import pandas as pd
import pickle
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.model_selection import train_test_split
# import xgboost as xgb
# from sklearn.model_selection import GridSearchCV
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.ensemble import RandomForestRegressor
# import statsmodels.api as sm




dosya2 = "model.save"
model = pickle.load(open(dosya2,"rb"))  



def convert_for_prediction(bedrooms,bathrooms,sqft_living,sqft_lot,floors,condition,sqft_above,sqft_basement,years_old,my_city):
    dosya = "sample.save"
    my_sample = pickle.load(open(dosya,"rb"))
    my_sample["bedrooms"] = bedrooms
    my_sample["bathrooms"] = bathrooms
    my_sample["sqft_living"] = sqft_living
    my_sample["sqft_lot"] = sqft_lot
    my_sample["floors"] = floors
    my_sample["sqft_above"] = sqft_above
    my_sample["sqft_basement"] = sqft_basement    
    my_sample["years_old"] = years_old
    the_city = "city_" + my_city
    my_sample[the_city] = 1
    return my_sample





def make_reshape(a_series):
    a_series = a_series.to_numpy()
    a_series = a_series.reshape(1, -1)
    return a_series



def round_1000_up(number):
    number = number * 1.03
    number = number // 1000
    number = number * 1000
    number = int(number)
    return number

    
def round_1000_down(number):
   number = number * 0.97
   number = number // 1000
   number = number * 1000
   number = int(number)   
   return number   

    
(4, 0.0, 0.0, 2000, 5000, 1.0, 1, 1000, 2000, 20, 'Algona', 44444)

def list_to_dict(my_list):
    my_dict={}
    my_dict["id"] = my_list[0]
    my_dict["bedrooms"] = my_list[1]
    my_dict["bathrooms"] = my_list[2]
    my_dict["sqft_living"] = my_list[3]
    my_dict["sqft_lot"] = my_list[4]
    my_dict["floors"] = my_list[5]
    my_dict["condition"] = my_list[6]
    my_dict["sqft_above"] = my_list[7]
    my_dict["years_old"] = my_list[8]
    my_dict["city"] = my_list[9]
    my_dict["prize"] = my_list[10]
    return my_dict



# test_x = convert_for_prediction(3,1,1000,2000,1,5,1000,2000,4,"Medina")

# test_x = make_reshape(test_x)

# file_name = "data.csv"

# data = pd.read_csv(file_name)

# data.drop(["date","street","statezip","country","yr_renovated","waterfront","view"], axis = 1, inplace = True )

# data["city"].value_counts()

# data = data[data["price"] > 10000]
# data = data[data["sqft_lot"] < 500000]

# data["yr_built"] = 2014 - data["yr_built"] 


# data = data.rename(columns={'yr_built': 'years_old'})


# datam = data[["bedrooms","bathrooms","floors","condition","city"]]



# data = pd.get_dummies(data)

# deneme123 = data.iloc[0,1:]

# my_sample = deneme123 * 0


# data.corr()



# x = data.drop(["price"],axis=1)

# y = data["price"]

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1,
#                                                     random_state=13)




# model = xgb.XGBRegressor(verbosity=1,random_state=13)

# model.fit(x, y)


# print("_" * 40)
# print(str(model))
# y_pred = model.predict(x_test)
# y_test = np.array(y_test)
# y_pred = pd.Series(y_pred)
# model_score = model.score(x_test, y_test)

# print("model score: ",model_score)




    
# compare_df = abs(y_pred - y_test).sort_values(ascending=False)


# model = sm.OLS(y_train,x_train).fit()
# print(model.summary())


# file_save_name = "sample.save"

# pickle.dump(my_sample,open(file_save_name,"wb"))




# <option value="1">One</option>
# <option value="2">Two</option>
# <option value="3">Three</option>

# pd.unique(pd.Series([2, 1, 3, 3]))

# def print_column_uniqe(df):
#     my_columns = list(df.columns)
#     for column in my_columns:
#         print(column,"\n")
#         print(list(pd.unique(datam[column])))
#         print("__" * 40)
        
# deneme = list(pd.unique(datam["bedrooms"]))
# print(deneme)

# print_column_uniqe(datam)

# condition = [3, 5, 4, 2, 1]
# condition.sort()

# floors = [1.5, 2.0, 1.0, 2.5, 3.0, 3.5]
# floors.sort()

# bathrooms = [1.5, 2.5, 2.0, 2.25, 1.0, 1.75, 2.75, 3.0, 3.25, 3.5, 8.0, 4.25, 4.0, 3.75, 5.0, 4.5, 5.75, 1.25, 6.5, 4.75, 0.75, 5.25, 5.5, 6.25, 0.0, 6.75]
# bathrooms.sort()

# city = ['Shoreline', 'Seattle', 'Kent', 'Bellevue', 'Redmond', 'Maple Valley', 'North Bend', 'Lake Forest Park', 'Sammamish', 'Auburn', 'Des Moines', 'Bothell', 'Federal Way', 'Kirkland', 'Issaquah', 'Woodinville', 'Normandy Park', 'Fall City', 'Renton', 'Carnation', 'Snoqualmie', 'Duvall', 'Burien', 'Covington', 'Inglewood-Finn Hill', 'Kenmore', 'Newcastle', 'Mercer Island', 'Black Diamond', 'Ravensdale', 'Clyde Hill', 'Algona', 'Skykomish', 'Tukwila', 'Vashon', 'Yarrow Point', 'SeaTac', 'Medina', 'Enumclaw', 'Snoqualmie Pass', 'Pacific', 'Beaux Arts Village', 'Preston', 'Milton']
# city.sort()

# bedrooms = [3, 5, 4, 2, 6, 7, 9, 1, 8, 0]
# bedrooms.sort()


# def convert_for_html(my_list):
#     for word in my_list:
#         print(f'<option>{word}</option>')
        
      
        
        
# print("condition\n")        
# convert_for_html(condition)
# print("__" * 40)
# print("floors\n")
# convert_for_html(floors)
# print("__" * 40)
# print("bathrooms\n")
# convert_for_html(bathrooms)
# print("__" * 40)
# print("city\n")
# convert_for_html(city)
# print("__" * 40)
# print("bedrooms\n")
# convert_for_html(bedrooms)



# print(list(data.columns))
# filehandler = open("sample.save","wb")
# my_sample = pickle.load(filehandler)









