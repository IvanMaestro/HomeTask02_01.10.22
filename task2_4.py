# 4.Реализуйте алгоритм перемешивания списка.

import random

# 1 вариант

# elem_num = int(input('Enter Number of elements: '))
# import random
# first_list = list()
# for j in range(0, elem_num):
#     first_list.append(j)


# print('-> ', first_list)
# second_list = random.shuffle(first_list)
# print('-> ', first_list)

# 2 вариант

n = int(input('Enter Number of elements: '))
first_list = [i for i in range(n)]
second_list = first_list[:]
for i in range(n):
    index_random = random.randint(0, n - 1)
    second_list[i], second_list[index_random] = second_list[index_random],second_list[i]
print('-> ', first_list)
print('-> ', second_list)
