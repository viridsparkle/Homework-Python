# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа 
# X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

# s = x + y
# p = x * y
# y = s - x
# p = (s - x) * x
# p = s * x - x * x
# x ** 2 - s * x + p == 0
x = 0
y = 0
d = s ** 2 - 4 * p
x == (-(-s) + d ** 0.5) // 2
y == s - x
if x + y == s and x * y == p:
    print(f"x = {x}, y = {y}")
else:
    x = (-(-s) - d ** 0.5) / 2
    y = s - x
    print(f"x = {x}, y = {y}")






# # y = p / x
# # s - x = p / x
# x = p / (s - x)
# p = x * (s - x)
# p = s * x - x ** 2

