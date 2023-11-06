import matplotlib.pyplot as plt

# создание файлов
Files = ["001.dat", "002.dat", "003.dat", "004.dat", "005.dat"]

colors = ['#00008B', '#1E90FF', '#006400', '#B23AEE', '#6959CD']

for i, file in enumerate(Files):

    fig, ax = plt.subplots()

    # считываем данные из файла
    with open(file, 'r') as f:
        n = int(f.readline())  # количество точек

        # собираем координаты точек
        X = []
        Y = []
        for _ in range(n):
            line = f.readline().split()  # разделение и сохранение в виде списка
            X.append(float(line[0]))
            Y.append(float(line[1]))

        ax.scatter(X, Y, color=colors[i], label=file, s=7)  # s-размер точек; label - файл в легенду

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.grid(linestyle='-', linewidth=1)
    plt.title('Number of points: ${}$'.format(n))
    plt.savefig('plot' + file + '.png')
    plt.show()

