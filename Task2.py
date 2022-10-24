# Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит 
# список простых множителей числа N.

# Натуральное число - любое число для счета от 0
# Простой множитель - это простые числа, которые делят это число нацело 


num = int(input("Введите натуральное число N: "))
i = 1 # первое простое число
lst = []
number = num
while i <= num:
    if num % i == 0: # True - значит делится без остатка
        lst.append(i)
        num //= i # делим нацело на i
        i = 2
    else:
        i += 1
        break
print(f"Простые множители числа {number} приведены в списке: {lst}")