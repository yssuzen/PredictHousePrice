import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#importing data set
df = pd.read_csv("multilinearregression.csv", sep=";")

#describe linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'roomnum', 'buildingage']], df['rent'])

#Taking area, number of rooms, and building age from user for predicting the price of the house
area = float(input('What is the area of the building: '))
roomNum = float(input('What is the number of rooms: '))
buildAge = float(input('What is the age of the building: '))

#making prediction
reg.predict([[area, roomNum, buildAge]])

#calculate the coefficient
reg.coef_

reg.intercept_



