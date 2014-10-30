Prereqs:
    - first 3 lessons of https://zapier.com/learn/apis/ (APIs, json, xml)
    - intro to html: first half of http://learn.shayhowe.com/html-css/building-your-first-web-page/
    - setup python environment (https://github.com/Yipit/yipit-wiki/wiki/Setting-up-the-dev-environment-lite.-%28for-Data-Analysts%29)
    - basic python scripting
    - chrome xpath extension https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl?hl=en

Comment on a blog post about stopping scrapers:
"Let me start by saying that I am a sadochist scraper and I will get your database if I want it. This goes the same for other scrapers who I am sure are more persistent than even I am. It will be more of a pain than usual, but I will get the data. I always get the data."


- why scrape? automated process to collect information from a website
    - can be less mistakes than human
    - can be scheduled to run
    - faster
    - restructure data
    - more extensible (change params)
    - more fun


- go to weather.gov
    http://forecast.weather.gov/MapClick.php?lat=42.070878306889426&lon=-72.62264907459428
    - view source + html101 reminder
- use requests in shell. grab page. print out data.
- explain lxml, etree, and then put xpath in from use xpath helper
- explain alternative xpaths and why
- move code to script and run via command line


- use chrome
    - go to http://www.sec.gov/cgi-bin/browse-edgar?company=groupon&owner=exclude&action=getcompany
    - look at inspect tab
- show how you would download/parse with curl/wget to grab reports
- quick intro to xpaths
- start a new script based on base.py. Go through and print out all report titles and bodies


- http://finance.yahoo.com/echarts?s=GRPN+Interactive
- explain how html can make additional requests. show network tab. find ajax call. remind about json



- from here can do insidermonkey or audience call
- insidermonkey example
- show chrome network tab. explain async calls
- use uncurl to show headers and user-agent?


bonus:
- regex
