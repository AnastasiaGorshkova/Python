import numpy as np
import os
import matplotlib.pyplot as plt

for path in os.listdir('./signals'):
    with open('./signals/' + path) as file:
        # initial = np.array(list(map(float, file.readlines())))  # массив исходных данных
        initial = np.loadtxt(file, dtype=float)

        # treated = np.array([np.mean(initial[max(0, i - 9): i + 1]) for i in range(np.size(initial))])
# массив обработанных данных: каждый элемент = среднее значение 10 предыдущих элементов (если они существуют)
# и текущего элемента массива исходных данных.

        base = np.ones(10) / 10
        treated = np.convolve(initial, base, mode='same')
# Создание окна с помощью np.ones(10) / 10 = массив из 10 элементов, каждый из которых равен 1/10.
# Функция np.convolve() = применение этого окна к массиву initial.
# Параметр mode='same' = размер итогового массива такой же, как и у исходного массива.

        fig, ax = plt.subplots()
        ax.plot(initial, linewidth=1, label='initial', color='#4682B4')
        ax.plot(treated, linewidth=2, color='#00008B', label='treated')

        plt.minorticks_on()  # вспомогательные деления на осях графика
        plt.grid(True, "major", "both", color="#888888")  # основная сетка
        plt.grid(True, "minor", "both", linestyle='--')  # вспомогательная сетка

        plt.legend()
        plt.title('Initial and Treated data for ' + path)
        plt.show()
