import pandas as pd
import matplotlib.pyplot as plt

# читаем файл
data = pd.read_csv('students.csv', sep=';', names=['Преподаватель', 'Группа', 'Оценка'])

# группируем по преподавателю и оценке
preps = data.groupby(['Преподаватель', 'Оценка']).size().unstack(fill_value=0)

# преподаватели - строки, оценки-столбики, значения- количество студентов со своей оценкой.
preps.plot(kind='bar', stacked=True)
plt.xlabel('Preps')
plt.ylabel('Students')
plt.title('Marks per prep')
plt.legend(title='Marks')
plt.savefig('preps.png')
plt.show()


# группируем по группе и оценке
groups = data.groupby(['Группа', 'Оценка']).size().unstack(fill_value=0)

groups.plot(kind='bar', stacked=True)
plt.xlabel('Groups')
plt.ylabel('Students')
plt.title('Marks per group')
plt.legend(title='Marks')
plt.savefig('groups.png')
plt.show()

