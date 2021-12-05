

def job():
    from csv import writer
    from pycoingecko import CoinGeckoAPI
    from csvEditor import dataAdd2
    import datetime
    #from practice import appendCSV
    # RUN THIS FILE TMR


    coinG = CoinGeckoAPI()
    todayData = coinG.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true',include_24hr_change='true')
    pr = todayData['bitcoin']['usd']
    mc = todayData['bitcoin']['usd_market_cap']
    VoL= todayData['bitcoin']['usd_24h_vol']
    Chge = todayData['bitcoin']['usd_24h_change']

    x = str(datetime.datetime.now())
    x = x.split(' ')
    
    #file = 'BTC.csv'
    file = 'BTCFILE.csv'

    newROW = [x[0], pr, mc, VoL, Chge, '0', '01']
    with open(file, 'a', newline='') as f_object:  
        # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(newROW)  
        # Close the file object
        f_object.close()


    dataAdd2(file)


job()

#### Below was uncommented if the job function call above is commented out
# using the below code you can run this file in terminal and it will add to the csv file whenever necessary


# import time
# import schedule

# schedule.every().day.at("00:00").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)