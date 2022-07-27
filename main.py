import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 OPR/40.0.2308.81',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'
}

"""response = requests.get("http://ledlife.by/raspisanie-2", headers=headers).text

soup = BeautifulSoup(response,"lxml")
table = soup.find('table')

data = pd.read_html(str(table))
data = data[0]
print(data)
data.to_csv('SDUSHOR.csv', index=False)

#---------

response = requests.get("https://chizhovka-arena.by/fizkultura-i-sport/katanie-na-konkah", headers=headers).text

soup = BeautifulSoup(response,"lxml")
table = soup.find('table')

data = pd.read_html(str(table))
data = data[0]
print(data)
data.to_csv('CHIZHOVKA.csv', index=False)

#---------
"""

response = requests.get("http://led.by/category/timetable/", headers=headers).text

soup = BeautifulSoup(response,"lxml")
content = soup.find('div', class_="postcontent")

dates = re.findall(r"(\d{2}.\d{2}.\d{2})",content.text)
dates1 =[]
for i in dates:
    if "-" not in i:
        dates1.append(i)

df = pd.DataFrame(dates1)
df.to_csv('PRITYCKOGO.csv', index=False)

times = re.findall(r"(\s\d{2}.\d{2}\s)",content.text)
times1 = []
for i in times:
    if "-" not in i:
        times1.append(i)

df = pd.DataFrame(times1)
df.to_csv('1.csv', index=False)


