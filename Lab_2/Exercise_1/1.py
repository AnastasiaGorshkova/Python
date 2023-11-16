import pandas as pd

# Чтение файла с данными
data = pd.read_csv('transactions.csv')

# Задача 1: Найдите 3 самых крупных платежа из реально проведённых (статус OK).
bigest = data[
    data['STATUS'] == 'OK'
            ].nlargest(3, 'SUM')  # из DF data выбираем строки, у которых 'STATUS' равно 'OK'
                                  # из отфильтрованных строк выбираем 3 строки с наибольшим значением в столбце 'SUM'

#сортируем по убыванию
big_sort = bigest.sort_values(by='SUM', ascending=False)

print("Топ 3 самых крупных платежа из реально проведённых:")

# Итерируем по каждой строке
for index, row in big_sort.iterrows():
    print(f"{row['CONTRACTOR']} - {row['SUM']}") #  Для каждой строки извлекаем значения столбцов 'CONTRACTOR' и 'SUM'


# Задача 2: Определите полную сумму реально проведённых платежей в адрес Umbrella, Inc.
#фильтруем по столбцу 'CONTRACTOR', оставляем только строки, где'Umbrella, Inc', а по 'STATUS', оставляем только 'OK'

total_umbrella = data[
    (data['CONTRACTOR'] == 'Umbrella, Inc') & (data['STATUS'] == 'OK')
                        ]['SUM'].sum()
print(f"Полная сумма реально проведенных платежей в адрес Umbrella, Inc: {total_umbrella}")