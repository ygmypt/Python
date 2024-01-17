import numpy as np

# Создание ряда от 0 до 100 с помощью NumPy
numbers = np.array(range(101))

# Вычисление суммы ряда
total_sum = np.sum(numbers)
print(total_sum)

import numpy as np

# Ввод числа с клавиатуры
n = int(input("Введите число: "))

# Создание ряда от 0 до введенного числа с помощью NumPy
numbers = np.array(range(n+1))

# Вычисление суммы ряда
total_sum1 = np.sum(numbers)
print("Сумма ряда от 0 до", n, "равна:", total_sum1)

import random

# Генерация 100 случайных чисел
random_numbers = [random.randint(1, 100) for _ in range(100)]

# Вычисление среднего
average = sum(random_numbers) / len(random_numbers)
print("Среднее среди 100 случайных чисел:", average)
