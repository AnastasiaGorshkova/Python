import matplotlib.pyplot as plt

# Читаем файл
with open('2.txt', 'r') as file:
    lines = file.readlines()

    # разбиваем на координаты X и Y
xs = []
ys = []
for i in range(0, len(lines), 2):
    xs.append(list(map(float, lines[i].split())))
    ys.append(list(map(float, lines[i + 1].split())))

for i in range(len(xs)):
    plt.figure()
    plt.plot(xs[i], ys[i])
    plt.xlim(0, 14)
    plt.ylim(-10, 10)
    plt.title(f'График {i+1}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig(f'График_{i+1}.png')
    plt.show()

