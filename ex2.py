# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input('Введите общее количество журавликов: '))
x = 0
# s = 2 * ( x + x ) + x + x = 4 * x + 2 * x = 6 * x
if s % 6 == 0:
    x = s // 6
    petya = x
    sereja = x
    kate = 4 * x
    print(f"Петя сделал {petya} журавликов")
    print(f"Сережа сделал {sereja} журавликов")
    print(f"Катя сделала {kate} журавликов")
else: print('Введенное число не соответствует условию задачи')
