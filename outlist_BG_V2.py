import csv
from pprint import pprint
import json
from TikTokApi import TikTokApi

out_list = []


def upload_data():
    global out_list
    with open('goog_list.csv', 'r', encoding='utf8') as ff:  # todo worked
        reader = csv.reader(ff)
        for i in reader:
            out_list.append(*i)
    out_list = out_list[1:]


# print(out_list)

# verifyFp = 'verify_kq112yue_2q65MEJ8_iWoy_4HXy_9R3D_WjXm0cNWJsq4'


# api = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

# tiktoks = api.trending()
# for i in tiktoks:
#     print(i['author']['uniqueId'])

# print(api.by_username('cutepetowner'))

ali = TikTokApi()


# search = ali.get_user('cutepetowner')  # Получить инфо о персоне #todo
# pprint(search)


# pprint(search)
# print(search['uniqueId'])

def find_videos(user_id):
    search = ali.by_username(user_id, count=11)

    # with open(f'search_{user_id}.json', 'w', encoding='utf8') as ff:  # todo запись ввиде словаря данных
    #     json.dump(search, ff)
    return search


def average_videos(data):
    """Средняя арифметическая просмотров видео"""
    all_views = 0
    for i in data[2:]:
        print(i['stats']['playCount'])
        all_views += i['stats']['playCount']
    average = all_views / 9
    return average


if __name__ == '__main__':
    # print(find_videos('cutepetowner')[1]['stats']['playCount'])
    print(average_videos(find_videos('cutepetowner')))
