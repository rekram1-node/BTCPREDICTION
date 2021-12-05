import pandas as pd
from pycoingecko import CoinGeckoAPI


def dataAdd2(fileName):
    cga = CoinGeckoAPI()
    data = cga.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true')
    prce = data['bitcoin']['usd']
    yesterDay = []
    # snapped_at,price,market_cap,total_volume,Yesterday_Price
    # snapped_at,price,market_cap,total_volume,Yesterday_Price,Day_Change,Tomorrow Price

    with open(fileName, 'r') as file:
        df = pd.read_csv(fileName)
        saved_column = df.price 
        for i, prce in enumerate(saved_column):
            if i != len(saved_column) - 1:
                yesterDay.append(prce)

    yesterDay.insert(0, yesterDay[0])
    #print(yesterDay[0], yesterDay[-1])

    df = pd.read_csv(fileName)
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)   # getting rid of unnamed columns that pandas creates
    df['Yesterday_Price'] = yesterDay
    df.to_csv(fileName, index = False)
    
    pandaData = pd.read_csv(fileName)
    dayChanges = []
    for P, Y in zip(pandaData['price'], pandaData['Yesterday_Price']):
        dayChange = float(P) - float(Y)
        dayChanges.append(dayChange)

    pandaData.drop(pandaData.columns[pandaData.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)   # getting rid of unnamed columns that pandas creates
    pandaData['Day_Change'] = dayChanges
    pandaData.to_csv(fileName, index = False)

    # adds tomorrow's price --- note doesn't have writing capability yet
    fileInformation = pd.read_csv(fileName)
    tomorrow = []

    for I, PRICE in enumerate(fileInformation['price']):
        if I+1 < len(fileInformation['price']):
            tomorrow.append(fileInformation['price'][I+1])


        else:
            tmr = []    # used to append past prices
            first = len(fileInformation['price']) -7 
            seventh = len(fileInformation['price'])  

            for elem in fileInformation['price'][first:seventh]:    # iterating through all the prices from a week ago to latest
                tmr.append(elem) # getting the last seven days of prices
            
            relations = [] # used to find relation between prices this week

            for tmrIndex, tmrElement in enumerate(tmr):
                if tmrIndex != 0: # if it is the first element it has nothing to subtract from
                    change = tmrElement - tmr[tmrIndex-1] # basically: today - yesterday 
                    relations.append(change) 

            relator = sum(relations) / len(relations) # finding the average relation
            tomorrowsAVG = sum(tmr) / len(tmr)   # finding the average price this week
            PredictionAverages = tomorrowsAVG + relator
            tomorrow.append(tomorrowsAVG + relator)

    fileInformation.drop(fileInformation.columns[fileInformation.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)   # getting rid of unnamed columns that pandas creates
    fileInformation['Tomorrow Price'] = tomorrow
    fileInformation.to_csv(fileName, index = False)  

#dataAdd2('BTC.csv')