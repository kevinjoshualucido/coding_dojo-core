''' 1. Update Values in Dictionaries and Lists '''

x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# 1.1
x[1][0] = 15
print(x)

# 1.2
students[0]['last_name'] = 'Bryant'
print(students[0])

# 1.3
sports_directory['soccer'][0] = 'Andres'
print(sports_directory["soccer"])

# 1.4
z[0]['y'] = 30
print(z)


print('-----')


''' 2. Iterate Through a List of Dictionaries '''

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterating_list_with_dict(some_list):
    for index_value in range(len(some_list)):
        for key, value in some_list[index_value].items():
            print(key, '-', value)


iterating_list_with_dict(students)


print('-----')


''' 3. Get Values From a List of Dictionaries '''


def list_with_dict_2(key_name, list):
    for index_val in range(len(list)):
        for key, value in list[index_val].items():
            if key == key_name:
                print(value)


list_with_dict_2('last_name', students)


print('-----')


''' 4. Iterate Through a Dictionary with List Values '''

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dojo_dict):
    for key, val in dojo_dict.items():
        print(len(val), key.upper())
        for instructors in range(len(val)):
            print(val[instructors])
        print('======')

print_info(dojo)


print('-----')