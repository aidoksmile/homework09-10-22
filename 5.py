# Реализуйте алгоритм перемешивания списка.

import random
def Fill_list(element):
    result = []
    fill_num = range(1, element + 1)
    numbers = list(fill_num)
    while len(numbers) > 0:
        i = random.randint(0, len(numbers) - 1)
        result.append(numbers[i])
        numbers.remove(numbers[i])
    return result

n = int(input('Введите число n = '))
print(Fill_list(n))