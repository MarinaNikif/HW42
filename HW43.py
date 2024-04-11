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
