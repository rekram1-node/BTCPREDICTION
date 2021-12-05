import pandas
from sklearn import linear_model
import csv
from csv import DictReader


                        # , chnge
def prediction1(volume, Yesterday, chnge):
    try:    
       
        df = pandas.read_csv("btccopy.csv") # , 'Day_Change'
        X = df[['total_volume', 'Yesterday_Price', 'Day_Change']]
        y = df['price']


        regr = linear_model.LinearRegression()
        regr.fit(X, y)              # 1000000000000
                                    #   1000000000000   , chnge
        predictedPrice = regr.predict([[ volume, Yesterday, chnge]])
        return predictedPrice

    except Exception as e: 
        print(e)

def findingYesterday(): # function that reads our file and finds yesterday's price by finding the last appended value
    yesterDay = []

    with open('BTC.csv', 'r') as file:
                dff = pandas.read_csv('BTC.csv')
                saved_column = dff.Yesterday_Price 
                for i, prce in enumerate(saved_column):
                        yesterDay.append(prce)
                

    yester = yesterDay[-1]  # this works, thought it didn't for a second
    return yester
