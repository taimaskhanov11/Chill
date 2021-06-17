import csv

out_list = []
with open('goog_list.csv', 'r', encoding='utf8') as ff:  # todo worked
    reader = csv.reader(ff)
    for i in reader:
        out_list.append(*i)
out_list = out_list[1:]
# print(out_list)