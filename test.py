from pprint import pprint

site = 'https://www.tiktok.com/@maksbraun'
import requests
from bs4 import BeautifulSoup

res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(res, 'lxml')
# print(res)
# print(res)
table_clips = soup.find_all(class_ ='count-infos')
print(table_clips)
for i in table_clips:
    print(i.text)