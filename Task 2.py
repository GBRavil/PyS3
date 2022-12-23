# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint
nums = []
n = int(input('Введите число '))
for i in range(n):
    nums.append(randint(-n,n))
print('Список элементов',nums)

mult = []
for i in range(n):
    