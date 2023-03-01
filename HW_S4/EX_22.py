# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
#  m - кол-во элементов второго множества.
#   Затем пользователь вводит сами элементы множеств.

# from random import randint

# def CreateTwoRandomLists(list1,list2):
#     n=int(input('введите n: '))
#     m=int(input('введите m: '))
#     for i in range(n):
#         list1.append(randint(-10, 10))
#     print(list1)
#     for j in range(m):
#         list2.append(randint(-10, 10))
#     print(list2)

# numbers1=[]
# numbers2=[]
# CreateTwoRandomLists(numbers1,numbers2)

# numbers3=((set(numbers1)).union(set(numbers2)))
# print(numbers3)


from random import randint
n=int(input('введите n: '))
list1 = [randint(1,10) for i in range(n)]
print(list1)

m=int(input('введите m: '))
list2 = [randint(1,10) for i in range(m)]
print()

list3=((set(list1)).union(set(list2)))
list3.sort()
print(list3)