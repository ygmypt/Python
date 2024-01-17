import numpy as np

number_matrix = np.loadtxt('C:\\temp\\numbermatrics.txt', delimiter=',')

dimension = int(np.sqrt(number_matrix.size))  # Определение размерности (предполагая, что это квадратная матрица)
identity_matrix = np.loadtxt('C:\\temp\\firstmatrics.txt', delimiter=',').reshape((dimension, dimension))

result_matrix = np.dot(number_matrix, identity_matrix)

np.savetxt('C:\\temp\\result_matrix.txt', result_matrix, delimiter=',', fmt='%d')

print(result_matrix)
