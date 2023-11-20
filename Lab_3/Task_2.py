import numpy as np
import os
import matplotlib.pyplot as plt

for path in os.listdir('./signals'):
    with open('./signals/' + path) as file:
        initial = np.array(list(map(float, file.readlines())))  # массив исходных данных
        treated = np.array([np.mean(initial[max(0, i - 9) : i + 1]) for i in range(np.size(initial))])
# массив обработанных данных: каждый элемент = среднее значение 10 предыдущих элементов (если они существуют)
# и текущего элемента массива исходных данных.

        fig, ax = plt.subplots()
        ax.plot(initial, linewidth=1, label='initial', color='#4682B4')
        ax.plot(treated, linewidth=2, color='#00008B', label='treated')

        plt.minorticks_on()  # вспомогательные деления на осях графика
        plt.grid(True, "major", "both", color="#888888")  # основная сетка
        plt.grid(True, "minor", "both", linestyle='--')  # вспомогательная сетка

        plt.legend()
        plt.title('Initial and Treated data for ' + path)
        plt.show()