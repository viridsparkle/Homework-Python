def fillData():
    data = []
    last_name = input('Введите фамилию: ')
    data.append(f' {last_name} ')
    first_name = input('Введите имя: ')
    data.append(f' {first_name} ')
    second_name = input('Введите отчество: ')
    data.append(f' {second_name} ')
    phone_number = input('Введите номер телефона: ')
    data.append(f' {phone_number} ')
    return data