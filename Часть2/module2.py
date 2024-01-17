import numpy as np

# Считывание числовой матрицы из файла
number_matrix = np.loadtxt('C:\\temp\\numbermatrics.txt', delimiter=',')

# Считывание единичной матрицы из файла
dimension = int(np.sqrt(number_matrix.size))  # Определение размерности (предполагая, что это квадратная матрица)
identity_matrix = np.loadtxt('C:\\temp\\firstmatrics.txt', delimiter=',').reshape((dimension, dimension))

# Умножение матриц
result_matrix = np.dot(number_matrix, identity_matrix)

# Запись результата в файл
np.savetxt('C:\\temp\\result_matrix.txt', result_matrix, delimiter=',', fmt='%d')

# Вывод результата
print(result_matrix)
