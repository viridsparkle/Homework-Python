from fill import fillData as get
def write_in_file():
    list = get()
    with open ('phones.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'{list[0]}  {list[1]}  {list[2]}  {list[3]}\n')
    with open ('phones.csv', 'a', encoding = 'utf-8') as data:
        data.write(f'{list[0]}  {list[1]}  {list[2]}  {list[3]}\n')