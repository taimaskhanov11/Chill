import csv
import datetime
import json
import random
import re
import string
import threading
from pprint import pprint

import gspread
import requests
from TikTokApi import TikTokApi
from bs4 import BeautifulSoup

from RW import time_track

headers = {
    "User-Agent": "Mozilla/5.0"
}
# verifyFp = 'verify_kq2i8rff_mKZjgffS_unpn_4vt5_AgDO_2c2JheLegA6Y'
# did = ''.join(random.choice(string.digits) for num in range(19))
# ali = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoint=True, custom_did=did)
ALI = TikTokApi()

acc_names = []

gc = gspread.service_account(filename='cedar-medley-310222-4f107bc4c913.json')

# sh = gc.open_by_url(
#     "https://docs.google.com/spreadsheets/d/18zSJudga-MZzI9cpZ_pAWYJcP8_f_gZ9x50vxY3eMN4/edit#gid=0")

# sh = gc.open_by_url(
#     'https://docs.google.com/spreadsheets/d/1NHLwajzW5uAvU3XBiYu-7lQj7Sir7-5JtkkmQlEriaQ/edit#gid=0')

sh = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1eFicSEX_HBfeq547SmLXb0rCzuO6vYsEwdst-FYFiBw/edit#gid=0')

worksheet = sh.sheet1


def download_data():
    """Загружает данные из таблицы в csv"""
    values_list = worksheet.col_values(1)  # todo worked
    print(values_list)
    values_list = [[i] for i in values_list]
    with open('goog_list1.csv', 'w', encoding='utf8', newline='') as ff:  # todo загружаем из таблицы адреса в csv
        writer = csv.writer(ff)
        for i in values_list:
            writer.writerow(i)


def correct_url(break_url):
    """Превращает адрес без логина в адресе с логином"""
    res = requests.get(break_url, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', property="og:url")
    if not acc_name:
        return False
    return acc_name.get('content')


def upload_data():
    """Выгрузка сайтов из cvs  для парсинга"""
    out_list = []
    with open('goog_list.csv', 'r', encoding='utf8') as ff:  # todo worked
        reader = csv.reader(ff)
        for i in reader:
            out_list.append(*i)
    out_list = out_list[1:]
    return out_list


def get_username(site):  # todo
    """Получение логина по адресу"""
    print(site)
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    try:
        # acc_name = soup.find('meta', property="og:url").get('content')
        acc_name = soup.find(class_='jsx-2997938848 share-title')
        print(acc_name)  # todo
        if not acc_name:
            acc_name = soup.find(class_='jsx-2997938848 share-title verified')
            if not acc_name:
                raise Exception
    except Exception as exp:
        print(f'Ошибка при получении логина {exp}')
        return False
    acc_names.append(acc_name)
    return acc_name.text.strip()


def find_videos(user_id):
    """Данные первых 11 видео"""
    search = ALI.by_username(user_id, count=11)
    # with open(f'search_{user_id}.json', 'w', encoding='utf8') as ff:  # todo запись ввиде словаря данных
    #     json.dump(search, ff)
    return search


def average_videos(data):
    """Средняя арифметическая просмотров видео"""
    all_views = 0
    for i in data[2:]:
        # print(i['stats']['playCount'])
        all_views += i['stats']['playCount']
    average = round(all_views / 9, 1)
    return average


def find_user_name(url):  # todo
    """Получение логина с помощю регулярного выражения"""
    search = re.search(r'com/@(.+)|com/(.+)', url)
    if search[1]:
        return search[1]
    elif search[2]:
        return search[2]
    else:
        print('Не найден логин')


def subscribers_count(user_name):
    return ALI.get_user(user_name)['userInfo']['stats']['followerCount']


def writing_file():  # todo
    pass


def changed(url, user_name, subscribers, average, date):
    """Изменение данных в таблице"""
    cell = worksheet.find(url)
    x, y = cell.row, cell.col
    print(f'Запись данных {url}')
    # worksheet.format(x, y+1, {'textFormat': {'bold': True}})
    worksheet.update_cell(x, y + 1, user_name)
    worksheet.update_cell(x, y + 2, subscribers)
    worksheet.update_cell(x, y + 3, average)
    worksheet.update_cell(x, y + 8, str(date))


def get_true_username(site):
    """Получение логина работает на всех адресах"""
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', attrs={'name': "keywords"}).get('content')
    if acc_name:
        acc_name = acc_name.split(',')[0].strip()
        return acc_name


def find_re_user_name(url):
    """Получение логина из url с помощью re"""
    search = re.search(r'@(\w+\.?\w+)\s?\)?', url)
    if search:
        return search[1]
    else:
        return False


def get_true_username_2(site):
    """Получение данных для извлечения логина"""
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', attrs={"property": "og:description"})
    print(acc_name)
    if acc_name:
        return acc_name.get('content')
    else:
        return False


ERRORS = []


@time_track
def end():
    worked_users = []
    with open('username_M_MULT.csv', 'r', encoding='utf8') as ff:
        reader = csv.reader(ff)
        for i in reader:
            worked_users.append(i)
    print(f'Всего {len(worked_users)}')
    for i in worked_users:

        url = i[0]
        user_name = i[1]
        try:
            videos = find_videos(user_name)
            average = average_videos(videos)
            subscribers = subscribers_count(user_name)
            date_string = datetime.datetime.now()
            date = date_string.strftime('%d.%m.%Y %H:%M:%S')
            print(f'Запись {url, user_name, subscribers, average, date}\n{"__" * 20}')
            changed(url, user_name, subscribers, average, date)
        except Exception as exp:
            print(exp)
            ERRORS.append((url, user_name))


@time_track
def create_dict():  # todo исправить re посик логина
    # todo создание нескоьких goole Api для соебинения с таблицей
    worked_users = []
    with open('username_M_MULT.csv', 'r', encoding='utf8') as ff:
        reader = csv.reader(ff)
        for i in reader:
            worked_users.append(i)
    print(f'Всего {len(worked_users)}')
    users_dict = []
    for i in worked_users:
        url = i[0]
        user_name = i[1]
        try:
            videos = find_videos(user_name)
            average = average_videos(videos)
            subscribers = subscribers_count(user_name)
            date_string = datetime.datetime.now()
            date = date_string.strftime('%d.%m.%Y %H:%M:%S')
            users_dict.append(
                {'url': url, 'user_name': user_name, 'subscribers': subscribers, 'average': average, 'date': date})
            print(f'Запись  в словарь {url, user_name, subscribers, average, date}\n{"__" * 20}')
            # break
        except Exception as exp:
            print(exp, url)
            ERRORS.append((url, user_name))
    pprint(users_dict)
    return users_dict

    # changed(url, user_name, subscribers, average, date)


if __name__ == '__main__':
    list_dict = create_dict()
    parsers = [
        threading.Thread(target=changed, args=(i['url'], i['user_name'], i['subscribers'], i['average'], i['date'])) for
        i in list_dict]
    for i in parsers:
        i.start()
    for i in parsers:
        i.join()



    # dowland_data()
    # url = 'https://vm.tiktok.com/ZSpyEnSu/'
    # url = 'https://www.tiktok.com/@milmraz'
    # user_name = get_username(url)
    # print(user_name)
    # user_name = find_user_name(url)
    # videos = find_videos(user_name)
    # average = average_videos(videos)
    # subscribers = subscribers_count(user_name)
    #
    #
    #
    # changed(url, user_name, subscribers, average)
