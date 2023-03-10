
def delete():
    data = open('HW/8/phones.csv', 'r', encoding = 'utf-8')
    search_query = input('Введите поисковой запрос: ')
    list = []
    count = 0
    for line in data:
        if search_query not in line:
            list.append(line)
        else: count += 1
    if count == 0:
        print('Данные отсутствуют')
    return list

