import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
}


def find_user_data(site):
    res = requests.get(site, headers=headers).text
    soup = BeautifulSoup(res, 'lxml')

    table_clips = soup.find_all(class_='number')
    acc_name = soup.find(class_='jsx-2997938848 share-title verified')  # todo
    subscribers = table_clips[1].find('strong').text  # todo

# likes # todo можно доработать
