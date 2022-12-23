# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
nums = []
n = int(input('Введите число '))
for i in range(n):
    nums.append(randint(0,n))
print(f'Список элементов {nums}')

r = round(n / 2 + 0.5) 
mult = []
for i in range(r):
    mult.append(randint(0,r))
for i in range(r):
    mult[i] = nums[i] * nums[n-1-i]
print(f'Произведение пар чисел {mult}')    