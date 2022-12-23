# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint
nums = []
n = int(input('Введите число '))
for i in range(n):
    nums.append(randint(-n,n))
print('Список элементов',nums)
sum = 0

for i in range(n):
    if i % 2 !=0:
        sum += nums[i]
        print(f'Элементы на нечетных позициях {nums[i]}')    
    else:
        sum 
print(f'Сумма элементов на нечетных позициях {sum}')       


