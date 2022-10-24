# Задача 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k.

# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x = 0

from random import randint
import itertools

k = randint(2, 7)

def get_list(k):
    list = [randint(0, 10) for i in range (k + 1)]
    while list[0] == 0:
        list[0] = randint(1, 10) 
    return 

def get_polynomial(k, list):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(list, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


list = get_list(k)
polynom1 = get_polynomial(k, list)
print(polynom1)

with open('file3.txt', 'w') as data:
    data.write(polynom1)

# не совсем разобралась, нашла в интернете. Посмотрю разбор на семинаре 5 (