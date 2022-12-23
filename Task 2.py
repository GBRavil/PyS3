# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
n = int(input('Введите число '))
nums = [randint(0,n) for i in range(n)]
print(f'Список элементов {nums}')
r = round(n / 2 + 0.5) 
mult = [nums[i]*nums[len(nums)-i-1] for i in range(r)]
print(f'Произведение пар чисел {mult}')  