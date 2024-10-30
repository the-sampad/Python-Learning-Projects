# Create a .env file first and store details in that
import requests
from twilio.rest import Client
from os import environ
from dotenv import load_dotenv

load_dotenv('F:\Python Practice\Day 36 - Stock Market\.env')

stock_url = "https://www.alphavantage.co/query"
news_url = "https://newsapi.org/v2/everything"

ACC_SID = environ.get('ACC_SID')
AUTH_TOKEN = environ.get('AUTH_TOKEN')

STOCK_NAME = 'TSLA'
COMPANY_NAME = 'Tesla Inc'

STOCK_API_KEY = environ.get('STOCK_API_KEY')
NEWS_API_KEY = environ.get('NEWS_API_KEY')

stock_parameters = {
    'apikey':STOCK_API_KEY,
    'symbol':STOCK_NAME,
    'function':'TIME_SERIES_DAILY',
}

stock_response = requests.get(stock_url,params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]

value_list = [value for (key,value) in stock_data.items()]
date_list = [key for (key,value) in stock_data.items()]

y_close = float(value_list[0]['4. close'])
dby_close = float(value_list[1]['4. close'])

diff = y_close - dby_close
abs_diff = abs(y_close - dby_close)
perc_change = (diff/dby_close)*100
perc_change = "%.2f"%perc_change

emoji = None
if diff >0 :
    emoji = '🔺'
else:
    emoji = '🔻'

if abs_diff>4:

    news_parameters = {
    'q':COMPANY_NAME,
    'from':date_list[1]+"T18:00:00Z",
    'to': date_list[0]+"T18:00:00Z",
    'apikey':'14babf1f9544440283855aa814d26d1d'
    }
    news_response = requests.get(news_url,params=news_parameters)
    news = news_response.json()["articles"]
    three_articles = news[:3]

    message_content = [f"{STOCK_NAME}:{emoji}{perc_change}%\nHeadline : {news['title']}\nBreaking News : {news['description']}" for news in three_articles]

    client = Client(ACC_SID, AUTH_TOKEN)
    for ar in message_content:

        message = client.messages\
            .create(
                body=ar,
                from_= '+12055513610',
                to='+917838238772'
        )
    print(message.status)
