import numpy as np
import matplotlib.pyplot as plt

with open('3.txt') as file:
    # data = np.array(list(map(float, file.readlines())))  # массив начальных данных
    data = np.loadtxt(file, dtype=float)
    A = np.identity(np.size(data))  # единичная матрица A, размер которой = размер массива data

    A[np.arange(np.size(data)), np.roll(np.arange(np.size(data)), 1)] = -1
    # Функция np.arange() = создание массива индексов от 0 до np.size(data) - 1
    # который представляет собой диагональные индексы в матрице A.
    # Функция np.roll() = сдвиг массива индексов на одну позицию влево (1).
    # В полученный сдвинутый массив индексов устанавливаем значение -1.

    # for i in range(np.size(data)):
    #     A[i, i - 1] = -1  # заполнение матрицы -1 под главной диагональю

    fig, ax = plt.subplots()
    while(1):  # бесконечный цикл
        done = 0
        plot, = ax.plot(data)
        plt.ion()  # интерактивный режим построения графиков
        plt.show()

        D = data

        plt.minorticks_on()  # вспомогательные деления на осях графика
        plt.grid(True, "major", "both", color="#888888")  # основная сетка
        plt.grid(True, "minor", "both", linestyle='--')  # вспомогательная сетка

        for i in range(255):
            D = D - 0.5 * A @ D
            plot.set_ydata(D)
            plt.pause(0.05)

            if(not plt.fignum_exists(fig.number)):  # если окно графика закрыли, то цикл прервался
                done = 1
                break

        if(done):
            break

        plt.pause(1)  # По завершении цикла пауза на 1 сек, а затем очистка осей графика
        ax.clear()

