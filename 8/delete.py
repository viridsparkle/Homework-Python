def delete():
    data = open('phones.csv', 'r', encoding = 'utf-8')
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

def rewrite():
    newList = delete()
    with open ('phones.csv', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}\n')
        data.close()
    with open ('phones.txt', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}\n')
        data.close()