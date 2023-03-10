def search():
    data = open('HW/8/phones.csv', 'r', encoding = 'utf-8')
    search_query = input('Введите поисковой запрос: ')
    flag = 1
    for line in data:
        if search_query in line:
            print(line)
            flag = 0
    if flag: print('Данные отсутствуют')

