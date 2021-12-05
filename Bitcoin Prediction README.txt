Bitcoin Prediction README


This text file will explain the way my bitcoin prediction program works


Side note: The prediction process is heavily reliant on the data in the
csv file named: "BTCFILE", this file was uploaded with up-to date data, but by the time it
if viewed by someone it will likely be not up to date. (If someone wanted to try this
program and have an updated csv file that will be detailed at the end.)


I apologize for the often silly variable names. This project was the first one I had to this scale and I did not realize how many functions or variables I would be needing at first. 


How it works:


Main file known as CoinRetriever.py has a function called RetrieveandPredict2. This function mainly uses the CoinGecko library to pull the current market cap, volume, day change, and yesterday’s opening price to predict what the price will be tomorrow at opening. CoinGecko considers the opening price to be the price at midnight. The program uses the previously mentioned values to pass to the function called predicitionLarge which uses the values and the BTCFILE.csv file to predict the opening price. The function largely rides on the multiple regression I imported from the sklearn library. The sklearn library that using linear multiple regression essentially uses the csv file previously mentioned and it reads certain columns from it such as price, market cap, etc and using these it creates a line of best fit for all the headers you want to use. Then using the .predict() function, we input today’s values that we want that were pulled from CoinGecko to find the location on the line based on the imputed values.


IF YOU WANT TO RUN THIS PROGRAM::::


Go to CoinGecko, look up Bitcoin, go to historical data, click download as csv file. Name your file ‘BTCFILE’ or change all the code that uses the file name to match yours. Then change the header of your csv file


from: snapped_at,price,market_cap,total_volume 
To: snapped_at,price,market_cap,total_volume,Yesterday_Price,Day_Change,Tomorrow Price


Then you can run the dataAdd2 function from the csvEditor program. Now your file is ready to run the coinRetriever program which will read the file and predict a price for Bitcoin. 


This is my first time writing an explanation for my code, I wanted this to be a simple and legible text document that is not too formal, thank you for your time.


* Aiden