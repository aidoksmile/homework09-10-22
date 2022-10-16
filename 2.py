# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def Factorial(element):
    result = 1
    if (element % 1 == 0 and element >= 1):
        for i in range(1, element +1 ):
            result = result * i
            print(result, end=' ')
    else:
        print('None')

print('Введите число:')
n = int(input())
Factorial(n)