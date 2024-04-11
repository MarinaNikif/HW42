import json

def normalize_key(key):
    return key.lower().replace('_', '')

def normalize_data(employee):
    return {normalize_key(k): v for k, v in employee.items()}

def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file:
        data = json.load(file)

    normalized_data = []
    for employee in data['employees']:
        normalized_employee = {}
        for k, v in employee.items():
            normalized_employee[normalize_key(k)] = v
        normalized_data.append(normalized_employee)

    lower_sort_type = normalize_key(sort_type)
    if lower_sort_type not in normalized_data[0]:
        raise ValueError(f'Key "{sort_type}" not found for sorting')

    sorted_data = sorted(normalized_data, key=lambda x: x[lower_sort_type])

    output_filename = f'employees_{sort_type}_sorted.json'
    with open(output_filename, 'w') as output_file:
        json.dump({"employees": sorted_data}, output_file, indent=4)

# Вызов функции для сортировки по фамилии ('lastName')
employees_rewrite('lastname')

# Вызов функции для сортировки по имени (firstName)
employees_rewrite('FIRSTName')

# Вызов функции для сортировки по отделу (department)
employees_rewrite('department')

# Вызов функции для сортировки по зарплате (salary)
employees_rewrite('SaLaRy')
