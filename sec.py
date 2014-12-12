import requests
from lxml import etree

url = "http://www.sec.gov/cgi-bin/browse-edgar?CIK=grpn&Find=Search&owner=exclude&action=getcompany"
res = requests.get(url)
parser = etree.HTMLParser()
root = etree.fromstring(res.content, parser)
document_urls = root.xpath('//*[@id="documentsbutton"]/@href')

for document_url in document_urls:
    url = "http://www.sec.gov{}".format(document_url)
    res = requests.get(url)
    parser = etree.HTMLParser()
    root = etree.fromstring(res.content, parser)
    rows = root.xpath('//*[@id="formDiv"]/div/table/tr')
    for row in rows:
        import pdb;pdb.set_trace()
        values = row.xpath("td")
        try:
            description = values[1].text
            doc_link = values[2].xpath("a")[0].attrib['href']
        except IndexError:
            continue

        url = "http://www.sec.gov{}".format(doc_link)
        res = requests.get(url)
        print description, res.text
