# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите длину массива: '))
list = []
for i in range(n):
    list.append(int(input(f"Введите {i+1}-е число массива: ")))
print(list)

x = int(input('Введите число X: '))
difMin = x - list[0]
nearestToX = 0
for i in range(1, len(list)):
    if list[i] < x:
        dif = x - list[i]
    elif x < list[i]:
        dif = list[i] - x
    else: dif = 0
    
    if dif < difMin:
        difMin = dif
        nearestToX = list[i]
print(f"Число, ближайшее к {x}: {nearestToX}")
    


