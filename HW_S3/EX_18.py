# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

N=int(input("введите количество элементов массива: "))
array = []
for i in range(N):
    array.append(randint(1, 5))
print(array)

result=0
x=int(input("введите число: "))
for i in range(len(array)):
    if abs(x-array[i])<abs(x-result):
        result=array[i]
print(result)

