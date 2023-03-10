from fill import fillData

def change():
    data = open('phones.csv', 'r', encoding = 'utf-8')
    search_query = input('Введите поисковой запрос: ')
    list = []
    count = 0
    for line in data:
        if search_query not in line:
            list.append(line)
        else: 
            new_line = ''.join(fillData())
            list.append(f'{new_line}\n')
            count += 1
    if count == 0:
        print('Данные отсутствуют')
    return list

def rewrite_change():
    newList = change()
    with open ('phones.csv', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}\n')
        data.close()
    with open ('phones.txt', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}\n')
        data.close()