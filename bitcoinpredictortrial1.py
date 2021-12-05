import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

def predictionLarge(marketcap, volume, Yesterday, price, dayChange):
    try:    
        df = pandas.read_csv("BTC.csv")

        X = df[['market_cap', 'total_volume', 'Yesterday_Price', 'price', 'Day_Change']]
        y = df['Tomorrow Price']

        regr = linear_model.LinearRegression()
        regr.fit(X, y)              # using multiple linear regression to find line of best fit

        predictedPrice = regr.predict([[marketcap, volume, Yesterday, price, dayChange]]) # using inputed values we find where the price is along the line of best fit
        return predictedPrice

    except Exception as e: 
        print(e)


