# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)

list = [int(input(f"Введите {i+1}-й элемент массива: ")) for i in range(10)]
min = int(input('Минимум = '))
max = int(input('Максимум = '))
print(f"Исходный массив: {list}")
list2 = []
for i in range(len(list)):
    if min <= list[i] <= max:
        list2.append(i)
print(f"Индексы элементов, находящихся в диапазоне от {min} до {max}: {list2}")