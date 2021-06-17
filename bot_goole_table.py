import re

import gspread

# Указываем путь к JSON
gc = gspread.service_account(filename='cedar-medley-310222-4f107bc4c913.json')
# Открываем тестовую таблицу
sh = gc.open("END")

# Выводим значение ячейки A1
# print(sh.sheet1.get('A1'))

# Вы можете открыть электронную таблицу по ее названию, как она отображается в Документах Google:
# worksheet = sh.get_worksheet(0)
# worksheet = sh.get_worksheet('имя')
# worksheet_list = sh.worksheets()
# worksheet = sh.sheet1
# val = sh.acell('C3').value
# print(worksheet_list)
# print(worksheet.acell('a1').value)

# Получить все значения из первой строки:

# values_list = worksheet.row_values(1)
# print(values_list)

# Получить все значения из первого столбца:
# values_list = worksheet.col_values(1)
# print(values_list)
# Получение всех значений из рабочего листа в виде списка словарей
# list_of_dicts = worksheet.get_all_records()
# print(list_of_dicts)

# Найти ячейку, соответствующую строке:
# cell = worksheet.find("Картошка")

# Найти ячейку, соответствующую регулярному выражению
# amount_re = re.compile(r'(Красная|Белая) картошка')
# cell = worksheet.find(amount_re)

# Найти все ячейки, соответствующие строке:
# cell_list = worksheet.findall("Красная картошка")

# Найти все ячейки, соответствующие регулярному выражению:
# criteria_re = re.compile(r'(Красная|Белая) картошка')
# cell_list = worksheet.findall(criteria_re)

# Обновление ячеек
# worksheet.update('B1', 'телефон')

# Или координаты строк и столбцов:
# worksheet.update_cell(1, 2, 'Свекла')
# Code language: JavaScript (javascript)

# Обновить диапазон
# worksheet.update('A1:B2', [[1, 2], [3, 4]])
