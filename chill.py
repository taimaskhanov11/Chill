import re

from END import upload_data, get_true_username
from selen import correct_url

site = 'https://www.tiktok.com/@egorkash?i.p_o?&fficial' #todo


def find_re_user_name(url):
    # print(url)
    # print(type(url))
    # print(str(url))
    # url = str(url)
    # search = re.search(r'com/@(.+)?|com/@(.+)|com/(.+)', url)
    # search = re.search(r'com/@?(\w+)\??', url) # todo без собачки
    search = re.search(r'com/@(\w+\.+\w+)\??', url)  # todo с собачкой
    if search:
        return search[1]
    else:
        return False
        # if search[1]:
        #     return search[1]
        # elif search[2]:
        #     return search[2]
        # elif search[3]:
        #     return search[3]


def find_correct_username():
    # print(find_re_user_name(site))
    for i in upload_data():
        if i:
            username = find_re_user_name(i)
            if not username:
                correct = correct_url(i)
                if correct:
                    """TRUE"""
                    username = find_re_user_name(correct)
                    if username:
                        print(i, username)
                else:
                    print(i, username, 'FALE')
            else:
                """TRUE"""
                print(i, username)

def find_true_username():
    for i in upload_data():
        username = get_true_username(i)
        print(i, username)

if __name__ == '__main__':
    find_correct_username()
    # print(find_re_user_name(site))
    # find_true_username()