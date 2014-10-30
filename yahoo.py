import datetime
import requests
from lxml import etree

url = "http://finance.yahoo.com/_td_charts_api/resource/charts;comparisonTickers=;events=div%7Csplit%7Cearn;gmtz=-4;indicators=quote;period1=1362251760;period2=1414610160;queryString=%7B%22s%22%3A%22GRPN%2BInteractive%22%7D;range=ytd;rangeSelected=undefined;ticker=GRPN;useMock=false?crumb=rhj3WXc6aYo"
res = requests.get(url)
close_prices = res.json()['data']['indicators']['quote'][0]['close']
timestamps = res.json()['data']['timestamp']

counter = 0
for timestamp in timestamps:
    real_date = datetime.datetime.fromtimestamp(timestamp)
    price = close_prices[counter]
    print real_date, price
    counter = counter + 1
