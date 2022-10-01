# Напишите программу, которая
# принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Введите число: '))


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


i = num
my_list = [0] * i
while i > 0:
    fact = factorial(i)
    my_list[i-1] = fact
    i -= 1

print(my_list)

# Другой вариант
# n = int(input('Введите число: '))
# m = 1
# res_list = []
# for i in range(1, n + 1):
#     m *= i
#     res_list.append(int(m))
# print(f'Набор произведений чисел от 1 до {n}: ', res_list)