def RetrieveandPredict2():
    from pycoingecko import CoinGeckoAPI
    from bitcoinpredictortrial1 import predictionLarge
    from bitPredicVOL_YESTERDAY import findingYesterday
    cg = CoinGeckoAPI()
    try:
        data = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true',include_24hr_change='true')
        price = data['bitcoin']['usd']
        mrkcap = data['bitcoin']['usd_market_cap']
        vol = data['bitcoin']['usd_24h_vol']
        change = data['bitcoin']['usd_24h_change']
        change *= 100
        Yestr = findingYesterday()

        predictedValue = str(predictionLarge(mrkcap, vol, Yestr, price, change))
    
        print("Predicted Price for Bitcoin is", predictedValue)
        print('\n')

        print(f"Today's price: {price} | Market Cap: {mrkcap} | Today's Volume: {vol} | 24hr change: {change} | Yesterday's Price: {Yestr}")
        print()
        return predictedValue
    except Exception as e:
        print(e)

RetrieveandPredict2()
