import requests
from lxml import etree

url = "http://www.sec.gov/cgi-bin/browse-edgar?company=groupon&owner=exclude&action=getcompany"
res = requests.get(url)
parser = etree.HTMLParser(encoding='UTF-8', strip_cdata=False)
root = etree.fromstring(res.content, parser)
relative_urls = root.xpath('//*[@id="documentsbutton"]/@href')
for relative_url in relative_urls:
    url = "http://www.sec.gov" + relative_url
    res = requests.get(url)
    root = etree.fromstring(res.content, parser)
    for report_row in root.xpath('//*[@id="formDiv"]/div/table/tr'):
        title = report_row.xpath("//td")[0].text
        relative_url = report_row.xpath("//td/a/@href")[0]
        report_body = requests.get("http://www.sec.gov" + relative_url)
        print title, report_body.content
