# Задача 5.
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

x = 0
y = 0


x = int(input('Введите коэффициант: '))
y = int(input('Введите коэффициант: '))

path = 'file1.txt'
data = open (path, 'r')
for line in data:
    print(line)
data.close()

path = 'file2.txt'
data = open (path, 'r')
for line in data:
    print(line)
data.close()

def init (a, b):
    global x
    global y
    x = a
    y = b


def sum():
    return a + b

# не совсем разобралась, пыталась как в Лекции сделать. 
# Посмотрю разбор на семинаре 5 (