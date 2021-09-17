"""
Домашнее задание №2
Работа csv
1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
import csv
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list = [
        {'name' : 'Olga', 'age' : 23, 'job' : 'engineer'},
        {'name' : 'Bob', 'age' : 21, 'job' : 'teacher'},
        {'name' : 'Alice', 'age' : 33, 'job' : 'programmer'}
    ]
    with open('list_1.csv', 'w', newline = '', encoding = 'utf - 8') as list_1:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(list_1, fields, delimiter=';')
        writer.writeheader()
        for member in list:
            writer.writerow(member)

if __name__ == "__main__":
    main()