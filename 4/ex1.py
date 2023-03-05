# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def sort(array):
    if len(array) <= 1:
        return array
    else:
        k = array[0]
    less = [i for i in array[1:] if i <= k]
    greater = [i for i in array[1:] if i > k]
    print(f"less = {less}, k = {[k]}, greater = {greater}")
    return (sort(less)+ [k] + sort(greater))


n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list1 = []
list2 = []
for i in range(n):
    list1.append(int(input(f"Введите {i+1}-й элемент 1-го множества: ")))
for i in range(m):
    list2.append(int(input(f"Введите {i+1}-й элемент 2-го множества: ")))
list1 = set(list1)
list2 = set(list2)
print(f"1 множество: {list1}")
print(f"2 множество: {list2}")
newList = list1.intersection(list2)
newList = list(newList)
print(f"Отсортированный по возрастанию список элементов, "
      f"встречающихся в обоих множествах: {(sort(newList))}")
