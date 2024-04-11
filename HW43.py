#
# Напишите функцию employees_rewrite(sort_type), которая:
#
#     Принимает параметром тип сортировки (ключ) - sort_type.
#     Функция должна:
#
# Получить данные из employees.json и записать в employees_[sort_type]_sorted.json:
#
#     Формат записи должен быть как в исходном файле.
#     Если сортировка производится по строковым значения, то в алфавитном порядке.
#     Если сортировка производится по числовым значениям, то в порядке убывания.
#
# Текстовый файл employees.csv, содержит данные о сотрудниках, их должности, и зарплате:
#
# {"employees":
#   [
#     {"firstName": "John",
#     "lastName": "Doe",
#     "department": "Marketing",
#     "salary": 50000},
#
#     {"firstName": "Alice",
#       "lastName": "Smith",
#       "department": "Engineering",
#       "salary": 60000},
#
#     {"firstName": "Bob",
#       "lastName": "Johnson",
#       "department": "Finance",
#       "salary": 55000}
#   ]
# }
#
# Выходные данные
# Результат записи в новый файл employees_lastname_sorted.json, если была вызвана функция в следующем виде - employees_rewrite('lastname'):
#
# {"employees":
#   [
#     {"firstName": "John",
#     "lastName": "Doe",
#     "department": "Marketing",
#     "salary": 50000},
#
#     {"firstName": "Bob",
#       "lastName": "Johnson",
#       "department": "Finance",
#       "salary": 55000},
#
#     {"firstName": "Alice",
#       "lastName": "Smith",
#       "department": "Engineering",
#       "salary": 60000}
#   ]
# }
#
# Примечания:
#
#     Если в функцию передаётся ключ, которого нет в словарях, то должно выбрасываться исключение - ValueError('Bad key for sorting')
#     Строки lastName, LASTNAME, Lastname и т.д. являются одними и те же ключами, старайтесь привести всё к одному формату при получении данных из файла и их записи.
#     Строки lastName и last_Name уже являются разными ключами, т.к. имею разное кол-во символов.

import json

def employees_rewrite(sort_type):
    # Загрузка данных из файла employees.json
    with open('employees.json', 'r') as file:
        data = json.load(file)

    # Проверка наличия указанного ключа для сортировки
    if sort_type not in data['employees'][0]:
        raise ValueError('Bad key for sorting')

    # Сортировка данных по указанному ключу
    sorted_data = sorted(data['employees'], key=lambda x: x[sort_type], reverse=(isinstance(data['employees'][0][sort_type], int)))

    # Запись отсортированных данных в новый файл
    output_filename = f'employees_{sort_type}_sorted.json'
    with open(output_filename, 'w') as output_file:
        json.dump({"employees": sorted_data}, output_file, indent=4)

# Вызов функции для сортировки по фамилии (lastName)
employees_rewrite('lastName')

# Вызов функции для сортировки по имени (firstName)
employees_rewrite('firstName')

# Вызов функции для сортировки по отделу (department)
employees_rewrite('department')

# Вызов функции для сортировки по зарплате (salary)
employees_rewrite('salary')