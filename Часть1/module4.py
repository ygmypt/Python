import numpy as np

numbers = np.array(range(101))

total_sum = np.sum(numbers)
print(total_sum)

import numpy as np

n = int(input("Введите число: "))

numbers = np.array(range(n+1))

total_sum1 = np.sum(numbers)
print("Сумма ряда от 0 до", n, "равна:", total_sum1)

import random

random_numbers = [random.randint(1, 100) for _ in range(100)]

average = sum(random_numbers) / len(random_numbers)
print("Среднее среди 100 случайных чисел:", average)
