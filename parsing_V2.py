from pprint import pprint
from outlist_BG_V2 import out_list

# site = f'{out_list[1]}'
site = f'https://www.tiktok.com/@kingpromotor'
print(site)
import requests
from bs4 import BeautifulSoup


headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Mobile Safari/537.36"
}


def get_data(url):
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 YaBrowser/21.5.3.742 Yowser/2.5 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print(r.text.encode('utf8'))
    r = r.text.encode('utf8')
    with open('index.html', 'wb') as ff:
        ff.write(r)


res = requests.get(site, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

# table_clips = soup.find_all(class_='number')
# acc_name = soup.find(class_='jsx-2997938848 share-title verified')  # todo
# subscribers = table_clips[1].find('strong').text  # todo
# likes # todo можно доработать

# if __name__ == '__main__':
#     print(soup.find(class_='jsx-4037782421 share-layout-header share-header'))
#     # get_data(site)
