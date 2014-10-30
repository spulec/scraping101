import requests
from lxml import etree

url = "FILL_ME_IN"
res = requests.get(url)
parser = etree.HTMLParser(encoding='UTF-8', strip_cdata=False)
root = etree.fromstring(res.content, parser)
import pdb;pdb.set_trace()