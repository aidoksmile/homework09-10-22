# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def Sum(element):
    result = 0
    i = 0
    for i in element:
        if (i != '.') and (i != '-'):
            result = result + int(i)
    return result

print('Введите число:')
n = float(input())
element = str(n)
print(Sum(element))