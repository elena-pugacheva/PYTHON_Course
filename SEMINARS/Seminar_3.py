
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# множество
# a={1, 1, 2, 0, -1, 3, 4, 4}
# print(len(a))

# list_1 = [1, 1, 2, 1, -1, 3, 4, 4]
# list_2 = []

# for i in list_1:
#     if i not in list_2:
#         list_2.append(i)
# print(len(list_2))

# list=set(spisok)
# print(len(list))




# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

# N = [12, 7, -1, 21, 0]

# k=3
# N = N[-k:] + N[:-k]
# print(N)

# spisok = [1, 2, 3, 4, 5, 6, 7]
# k = int(input('Введите число сдвига: '))
# temp = None
# for i in range(0, k):
#     for j in range(len(spisok)-1, 0, -1):
#         temp = spisok[j]
#         spisok[j] = spisok[j-1]
#         spisok[j-1]= temp
# print(spisok)

# Напишите программу 
# для печати всех уникальных значений в словаре.

# spisok = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#           {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"},
#           {" VIII ": "S007"}]
# result = list()
# for dict in spisok:
#     for k in dict:
#         result.append(dict[k])
# print(set(result))

# Дан массив, состоящий из целых чисел. 
# Напишите программу, которая подсчитает 
# количество элементов массива, больших 
# предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
#  Output: 2 (-1 < 5, 2 < 3)

# list=[0, -1, 5, 2, 3]
# count=0

# for i in range(len(list)-1):
#     if list[i]<list[i+1]:
#         count+=1
# print(count)

