import requests
from lxml import etree

url = "http://forecast.weather.gov/MapClick.php?lat=42.070878306889426&lon=-72.62264907459428"
res = requests.get(url)
parser = etree.HTMLParser()
root = etree.fromstring(res.content, parser)
element = root.xpath('//*[@id="current_conditions"]/div[2]/p[2]')[0]
print element.text
