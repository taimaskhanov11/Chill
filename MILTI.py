import csv
import re
import threading
import time

import requests
from bs4 import BeautifulSoup

from END import upload_data
from RW import time_track

headers = {
    "User-Agent": "Mozilla/5.0"
}

USER_LIST = []


def get_true_username_2(site):
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')
    acc_name = soup.find('meta', attrs={"property": "og:description"})
    print(acc_name)
    if acc_name:
        return acc_name.get('content')
    else:
        return False


def find_re_user_name_2(url):
    # search = re.search(r'@(\w+)\s?\)?', url)  # todo с собачкой
    # print(f'RE{url}')
    # search = re.search(r'@(\w+\.?)\s?\)?', url)  # todo с собачкой
    search = re.search(r'@(\w+\.?\w+)\s?\)?', url)  # todo с собачкой
    if search:
        return search[1]
    else:
        return False


class PageSizer(threading.Thread):

    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.USER_LIST = []
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }

    def run(self):
        self.USER_LIST = []
        print(f'Загрузка...{self.url}')
        if not self.url:
            return
        data = self.get_data(self.url)
        if data:
            username = self.find_re(data)
            if username:
                print(f'Запись {self.url, username}')
                USER_LIST.append([self.url, username])
                self.USER_LIST = [self.url, username]
            print(self.url, username)
        else:
            print(self.url, data)

    def find_re(self, url):
        search = re.search(r'@(\w+\.?\w+)\s?\)?', url)  # todo с собачкой
        if search:
            return search[1]
        else:
            return False

    def get_data(self, site):
        res = requests.get(site, headers=self.headers).text
        soup = BeautifulSoup(res, 'lxml')
        acc_name = soup.find('meta', attrs={"property": "og:description"})
        if acc_name:
            return acc_name.get('content')
        else:
            return False


def nain():
    urls = upload_data()
    sizers = []
    print(len(urls))
    for i in upload_data():
        # print(i)
        if i:
            sizers.append(PageSizer(i))
    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()
    print(f'Общие Данные{USER_LIST}')
    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.USER_LIST}')
    with open('username_MULTI.csv', 'w', encoding='utf8', newline='') as ff:  # todo загружаем из таблицы адреса в csv
        writer = csv.writer(ff)
        for i in USER_LIST:
            writer.writerow(i)


def test():
    liste = []
    data = upload_data()
    print(len(data))
    for i in data[:50]:
        if i:
            liste.append(threading.Thread(target=get_true_username_2, args=(i,)))
    for i in liste:
        i.start()
    for i in liste:
        i.join()
    liste = []
    for i in data[50:100]:
        if i:
            liste.append(threading.Thread(target=get_true_username_2, args=(i,)))
    for i in liste:
        i.start()
    for i in liste:
        i.join()


def start_milti(urls, x, y):
    global USER_LIST
    USER_LIST = []
    print(len(urls))
    print(urls, x, y)
    sizers = [PageSizer(url=url) for url in urls[x:y]]
    for sizer in sizers:
        sizer.start()
    for sizer in sizers:
        sizer.join()
    # print(f'Общие Данные{USER_LIST}')
    for sizer in sizers:
        print(f'For url {sizer.url} need download {sizer.USER_LIST}')
    with open(f'username_M_MULT.csv', 'a', encoding='utf8',
              newline='') as ff:  # todo загружаем из таблицы адреса в csv
        writer = csv.writer(ff)
        for i in USER_LIST:
            writer.writerow(i)


@time_track
def main():
    urls = upload_data()
    const = len(urls) // 7
    for i in range(0, 247, const):
        print(i, const + i)
        start_milti(urls, i, const + i)


if __name__ == '__main__':
    main()
