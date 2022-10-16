# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

def Fill_list(element):
    positions = []
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        positions.append(int(line))
    data.close()
    d = 1
    i = 0
    for number in range(- element, element + 1):
        if i in positions:
            d = d * number
        print (i, ":" ,number) 
        i += 1
    return d

n = int(input('Введите число n = '))
print(Fill_list(n))