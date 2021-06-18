import csv
import datetime
import threading
import time

from END import find_videos, average_videos, subscribers_count, changed
from TikTokApi import TikTokApi
ERRORS = []

class TableWrite(threading.Thread):

    def __init__(self, url, username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
        self.username = username

    def run(self):
        try:
            tipe = TikTokApi()
            videos = find_videos(self.username, tipe)
            average = average_videos(videos)
            subscribers = subscribers_count(self.username, tipe)
            date_string = datetime.datetime.now()
            date = date_string.strftime('%d.%m.%Y %H:%M:%S')
            print(f'Запись {self.url, self.username, subscribers, average, date}\n_*20')
            changed(self.url, self.username, subscribers, average, date)
        except Exception as exp:
            print(exp)
            ERRORS.append((self.url, self.username))


def end():
    worked_users = []
    with open('username_M_MULT.csv', 'r', encoding='utf8') as ff:
        reader = csv.reader(ff)
        for i in reader:
            worked_users.append(i)
    quantity = len(worked_users)
    print(quantity)
    sizers = [TableWrite(url=i[0], username=i[1]) for i in worked_users[:quantity // 2]]
    for sizer in sizers:
        time.sleep(2)
        sizer.start()
    for sizer in sizers:
        sizer.join()

    sizers = [TableWrite(url=i[0], username=i[1]) for i in worked_users[quantity // 2:]]
    for sizer in sizers:
        time.sleep(2)
        sizer.start()
    for sizer in sizers:
        sizer.join()

    print(ERRORS)
    # url = i[0]
    # user_name = i[1]
    # videos = find_videos(user_name)
    # average = average_videos(videos)
    # subscribers = subscribers_count(user_name)
    # date_string = datetime.datetime.now()
    # date = date_string.strftime('%d.%m.%Y %H:%M:%S')
    # changed(url, user_name, subscribers, average, date)


if __name__ == '__main__':
    end()
