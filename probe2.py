import csv
from pprint import pprint

from MILTI import main
from selen import upload

# upload()
main()
LIST = []
LIST2 = []

with open('username_M_MULT.csv', 'r', encoding='utf8') as ff:  # todo загружаем из таблицы адреса в csv
    reader = csv.reader(ff)
    for i in reader:
        LIST.append(i[0])

with open('usernameSTATIC.csv', 'r', encoding='utf8') as ff:  # todo загружаем из таблицы адреса в csv
    reader = csv.reader(ff)
    for i in reader:
        LIST2.append(i[0])

for i in LIST:
    if i not in LIST2:
        print(i)
print('___')
for i in LIST2:
    if i not in LIST:
        print(i)

pprint(len(LIST))
pprint(len(LIST2))
print(sorted(LIST) == sorted(LIST2))
