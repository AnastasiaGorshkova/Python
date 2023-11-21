import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

with open('main.txt') as file:
    n = file.readline()
    data = np.loadtxt(file, dtype=float)
    A = data[:-1]  # строки с коэффициентами матрицы A
    b = data[-1]  # последняя строка с вектором b

x = solve(A, b)  # решение системы

fig, ax = plt.subplots()
xs = np.arange(0, x.size, 2).astype(str)
ax.bar(xs, x[::2])
ax.grid(True, "major", "both", color="#888888")
ax.set_xlabel('Номер вектора x[i]')
ax.set_ylabel('Решение x=Ab')

plt.savefig('Результат.png')
plt.show()

