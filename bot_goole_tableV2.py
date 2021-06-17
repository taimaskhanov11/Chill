from pprint import pprint
import csv
import gspread

# Указываем путь к JSON


gc = gspread.service_account(filename='cedar-medley-310222-4f107bc4c913.json')
# Открываем тестовую таблицу

# sh = gc.open("END")#todo
sh = gc.open_by_url(
    'https://docs.google.com/spreadsheets/d/1NHLwajzW5uAvU3XBiYu-7lQj7Sir7-5JtkkmQlEriaQ/edit#gid=0')  # todo worked
worksheet = sh.sheet1
# print(sh.sheet1.get())
# worksheet_list = sh.worksheets()
# print(worksheet_list)
# cell = worksheet.acell('B1', value_render_option='FORMULA').value
# print(cell)
# values_list = worksheet.col_values(1)
# pprint(values_list)#todo
list_of_lists = worksheet.get_all_values()  # todo worked
list_of_dicts = worksheet.get_all_records()  # todo worked
# pprint(list_of_dicts)
cell = worksheet.find("https://www.tiktok.com/@adam.rich")  # todo worked
# print(cell.row, cell.col)
# print(cell.)
# print(worksheet.cell(131, 2).value)
# val = worksheet.acell('B2').value
# print(val)

values_list = worksheet.col_values(1)  # todo worked
# print(values_list)
# values_list = [[i] for i in values_list]


# with open('goog_list.csv', 'w', encoding='utf8', newline='') as ff: # todo загружаем из таблицы адреса в csv
#     writer = csv.writer(ff)
#     for i in values_list:
#         writer.writerow(i)
#
out_list = []
with open('goog_list.csv', 'r', encoding='utf8') as ff:  # todo worked
    reader = csv.reader(ff)
    for i in reader:
        out_list.append(*i)
out_list = out_list[1:]
print(out_list)
# with open('goog_list.txt', 'w', encoding='utf8') as ff:
#     # ff.writelines(values_list)
#     ff.writelines("%s\n" % line for line in values_list)
#     # for i in values_list:
#     #     ff.write(i)

# out_list = []
# with open('goog_list.txt', 'r', encoding='utf8') as ff:
#     for i in ff:
#         out_list.append(i)
#
# print(out_list)
