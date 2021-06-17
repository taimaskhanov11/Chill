from pprint import pprint
from outlist_BG_V2 import out_list


site = f'{out_list[1]}'
print(site)
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