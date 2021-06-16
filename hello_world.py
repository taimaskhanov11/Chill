import csv
import unicodedata
from pprint import pprint

import requests
from bs4 import BeautifulSoup
import json

# from Nothing.asd import time_track

all_data_list = []


def find_sites():
    for i in all_data_list[1:]:
        all_stocks_dict = []
        site = f'{i[0]}'
        if not site:
            return
        print(site)
        # site = 'https://broker.ru/quotes/foreign'
        res = requests.get(site, headers={"User-Agent": "Mozilla/5.0"}).text
        soup = BeautifulSoup(res, 'lxml')
        try:
            acc_name = soup.find(class_='jsx-2997938848 share-title verified').text
            print(f'название аккаунта {acc_name}')
            subscribers = soup.find(class_='count-infos').find_all('strong')[1].text
            # print(subscribers)
            print(f'Подписчики {subscribers}')
            # average_views = soup.find(class_ ='jsx-1400010900 video-feed compact')
            
            print(soup.find(class_ ='tt-feed'))
            # for i in average_views.find_all('div'):
            #     print(i)
                # print(i.find_all(class_='jsx-1036923518 video-count'))



            break
        except AttributeError as exp:
            print(exp)
            # print("Переадресация")
            # acc_name = soup.find('body')
            # print(acc_name.text)
            # break

        # break
        # for item in all_product_hrefs:
        #     # print(item.span.parent)
        #     # print(item)
        #     item.span.decompose()
        #     # print(item)
        #     # # print(a)
        #     # break
        #     item_text = item.text.strip()
        #     item_href = 'https://broker.ru/' + item.get('href')
        #     all_site_list[item_text] = item_href
        # with open(f'jsin_dict/{i}_all_stocks_dict.json', mode='w') as ff:
        #     json.dump(all_site_list, ff, indent=4, ensure_ascii=False)
        # all_stocks_dict.append(all_site_list)

        # print(i)
    # with open(f'all_stocks_dict.json', mode='w') as ff:
    #     json.dump(all_stocks_dict, ff, indent=4, ensure_ascii=False)


with open(f'tg_copy.csv', 'r', encoding='ascii', errors='ignore') as ff:
    reader = csv.reader(ff)
    ciunt = 0
    for i in reader:
        if i:
            all_data_list.append(i)

# for i in all_data_list[1:]:
# print(i)
# break

if __name__ == '__main__':
    find_sites()
    # pprint(all_data_list)
