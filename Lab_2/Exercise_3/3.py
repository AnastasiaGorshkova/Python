import pandas as pd
import matplotlib.pyplot as plt

# Задача 1: постройте графики среднего количества решённых задач (а) по факультетским группам, (б) по группам по информатике.
# Формат графика - любой достаточно наглядный.


# Загрузка данных из файлов в новые DF
students_info = pd.read_excel('students_info.xlsx')
results_ejudge = pd.read_html('results_ejudge.html')[0]
# [0] указывает на то, что мы выбираем первую таблицу из списка таблиц, полученных с помощью pd.read_html.

# Объединение данных по логину студента
merged_data = results_ejudge.merge(students_info, left_on='User', right_on='login')

# Расчитываем среднее количество решенных задач по факультетским группам (для графика (а))
mean_faculty_group = merged_data.groupby('group_faculty')['Solved'].mean()

# Расчитываем среднее количество решенных задач по группам по информатике (для графика (б))
mean_informatics_group = merged_data.groupby('group_out')['Solved'].mean()

# Построение графика для среднего количества решенных задач по факультетским группам
plt.figure(figsize=(10, 6))
mean_faculty_group.plot(kind='bar', color='#7FFFD4', title='Среднее количество решенных задач по факультетским группам')
plt.xlabel('Факультетская группа')
plt.ylabel('Среднее количество решенных задач')
plt.xticks(rotation=45)
plt.grid(linestyle='--', alpha=0.7)
plt.show()

# Построение графика для среднего количества решенных задач по группам по информатике
plt.figure(figsize=(10, 6))
mean_informatics_group.plot(kind='bar', color='#00BFFF', title='Среднее количество решенных задач по группам по информатике')
plt.xlabel('Группа по информатике')
plt.ylabel('Среднее количество решенных задач')
plt.xticks(rotation=45)
plt.grid(linestyle='--', alpha=0.7)
plt.show()



# Задача 2: определите, из каких факультетских групп пришли и в какие группы по информатике попали люди,
# которые смогли пройти более одного теста в хотя бы одной из двух последних задач.
# (Задачи G и H в таблице, каждый тест даёт 10 баллов.) Рисовать график не обязательно, можно просто цифры посчитать.


# Определение студентов, прошедших более одного теста в задачах G и H
student_tests = results_ejudge[
    (results_ejudge['G'] > 1) | (results_ejudge['H'] > 1)
                              ]

# Объединение данных о студентах с данными из students_info
tests = student_tests.merge(students_info, left_on='User', right_on='login')

# Определение факультетских групп и групп по информатике студентов
faculty_group = tests['group_faculty']
informatics_group = tests['group_out']
result_1 = faculty_group.value_counts()
result_2 = informatics_group.value_counts()
print("Факультетские группы студентов, прошедших более одного теста в задачах G и H:")
print(result_1.to_string())
print("Группы по информатике студентов, прошедших более одного теста в задачах G и H:")
print(result_2.to_string())

