def rewrite(function):
    newList = function
    with open ('HW/8/phones.csv', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}')
        data.close()
    with open ('HW/8/phones.txt', 'w', encoding = 'utf-8') as data:
        for i in range(len(newList)):
            data.write(f'{newList[i]}')
        data.close()