# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

N=int(input("введите количество элементов массива: "))
array = []
for i in range(N):
    array.append(randint(-10, 10))
print(array)

min=int(input('min: '))
max=int(input('max:'))
result=[]
for i in range (len(array)):
    if min<array[i]<max:
        result.append(i)
print(result)