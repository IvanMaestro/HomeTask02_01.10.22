# Напишите программу, 
# которая принимает 
# на вход вещественное 
# число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

n = input("Введите дробное число: ")

print('Сумма цифр в числе -> ', sum(map(int, list(n.replace(".", "")))))
