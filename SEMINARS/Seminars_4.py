# ФУНКЦИИ И РЕКУУРСИЯ. МЕТОД БЫСТРОЙ СОРТИРОВКИ И МЕТОД СЛИЯНИЯ.

def sumNumbers(n):

    summa = 0
    for i in range(1, n + 1):
        summa += i
        return summa

    n = int(input())  # 5
    print(sumNumbers(n))  # 15
