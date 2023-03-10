def create():
    list1 = []
    list1.append('Фамилия')
    list1.append('Имя')
    list1.append('Отчество')
    list1.append('Номер телефона')
    with open('phones.csv', 'w', encoding = 'utf-8') as info:
        info.write(f"{list1}\n")
    with open('phones.txt', 'w', encoding = 'utf-8') as info:
        info.write(f"{list1}\n")