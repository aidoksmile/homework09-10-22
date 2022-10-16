# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

my_dict = {}
n = 6
for i in range(1, n+1):
    my_dict[i] = 3*i +1
print(my_dict)