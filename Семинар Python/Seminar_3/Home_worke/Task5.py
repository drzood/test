# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# Пример:
#     - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)


# num = int(input('Введите целое число: '))  # ввод


# def fib(n):          # рекурсивный метод фиббоначи
#     if n in [1, 2]:  # если в переменной н 1 или два то возвращаем 1
#         return 1
#     else:            # тогда (метод - 1) + ( метод - 2)
#         return fib(n - 1) + fib(n - 2)


# def neg_fib(n):      # рекурсивный метод негофиббоначи
#     if n == 0:       # если н = 0 то возвращаем 0
#         return 0
#     if n == 1:       # если н = 1 то возвращаем рекурсивный метод -1+1
#         return neg_fib(n - 1) + 1
#     else:            # тогда (метод - 2) - (метод - 1)
#         return (neg_fib(n - 2) - neg_fib(n - 1))


# list_fib = []        # создаем пустой список
# for e in range(1, num + 1): # цикл от 1 до вводной переменной    
#     list_fib.append(fib(e)) # заполнянм список используя метод фиб

# list_neg_fib = []    # создаем пустой список
# for e in range(num, -1, -1): # цикл от -1 до переменной нам
#     list_neg_fib.append(neg_fib(e)) # заполняем список используя метод нег_фиб

# print(list_neg_fib + list_fib) # вывод список нег_фиб + список фиб



# def lst_fibonacci_num():
#     num = int(input('Введите любое натуральное число: '))
#     fib = []
#     a, b = 1, 1
#     for i in range(num):
#         fib.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for j in range(num + 1):
#         fib.insert(0, a)
#         a, b = b, a - b
#     print(f'Список чисел Фибоначчи для {num}: {fib}')


# lst_fibonacci_num()

import random
a = random.randint(5, 11)
b = [1, 1]
[b.append(b[i-2] + b[i-1]) for i in range(2, a)]
[b.insert(0, b[1] - b[0]) for i in range(a + 1)]
print(b)