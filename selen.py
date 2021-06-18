import csv
import re
import threading
from pprint import pprint

import requests
from bs4 import BeautifulSoup
from END import upload_data
import time

# from END import get_username

# site = 'https://www.tiktok.com/@egorkaship_official'
# site = 'https://vm.tiktok.com/ZSpyEnSu/'
# site = 'https://www.tiktok.com/@zhanna_mood?_r=1'
# site = 'https://www.tiktok.com/@nastpavlova.hi'
# site = 'https://www.tiktok.com/@maksbraun'
site = 'https://www.tiktok.com/@el_alekperov'
from RW import time_track

# site = 'https://vm.tiktok.com/ZS9vnf93/'

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(site, headers=headers).text
soup = BeautifulSoup(res, 'lxml')


# print(res)

# with open('index.html', 'w', encoding='utf8') as ff:#todo Запись в html
#     ff.write(res)

# with open('index.html', 'r', encoding='utf8') as ff:
#     ff.write(res)


# print(soup.find())

def find_re_user_name_2(url):
    # search = re.search(r'@(\w+)\s?\)?', url)  # todo с собачкой
    # print(f'RE{url}')
    # search = re.search(r'@(\w+\.?)\s?\)?', url)  # todo с собачкой
    search = re.search(r'@(\w+\.?\w+)\s?\)?', url)  # todo с собачкой
    if search:
        return search[1]
    else:
        return False


def correct_url(break_url):
    """Превращает адрес без логина в адресе с логином"""
    res = requests.get(break_url, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', property="og:url")
    if not acc_name:
        return False
    return acc_name.get('content')


# username = get_username(site)
# if not username:
#     site = correct_url(site)
#     print(site)
#     username = get_username(site)
# print(username)

# username = get_username('https://www.tiktok.com/@zhanna_mood?_r=1')
# print(username)


# print(res)
# with open(f'egorkaship_official.html', 'w', encoding='utf8') as ff:
#     ff.write(res)

def get_true_username_2(site):
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', attrs={"property": "og:description"})
    if acc_name:
        return acc_name.get('content')
    else:
        return False


USER_LIST = []


@time_track
def upload():
    count = 0
    for i in upload_data():
        count += 1
        # print(i)
        if i:
            data = get_true_username_2(i)
            # print(data)
            if data:
                # print(f'LIST {data}')
                username = find_re_user_name_2(data)

                if username:
                    USER_LIST.append([i, username])
                print(i, username)
            else:
                print(f"Не прошел проверку{count} - {i} leve 2")

                # print(i, data)
        else:
            print(f"Не прошел проверку{count} - {i} leve 1")
            # print(i)
    # user_list = [[i] for i in USER_LIST] #todo
    with open('usernameSTATIC.csv', 'w', encoding='utf8', newline='') as ff:  # todo загружаем из таблицы адреса в csv
        # pprint(USER_LIST)
        writer = csv.writer(ff)
        for i in USER_LIST:
            writer.writerow(i)


if __name__ == '__main__':
    # list_user = get_true_username_2('https://www.tiktok.com/@jagr.mlb') #todo исправить http запрос
    # username = find_re_user_name_2(list_user)     # todo исправить re
    # print(list_user)
    upload()
    # data = get_true_username_2('https://www.tiktok.com/@anastasia_yseeva_17')
    # username = find_re_user_name_2(data)
    # print(username)
