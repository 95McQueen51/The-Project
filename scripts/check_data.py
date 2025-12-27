Проверка данных в CSV.

python
import pandas as pd

df = pd.read_csv("data.csv")

print("Количество записей:", len(df))
print("Студенты:", df["student"].unique())
print("Предметы:", df["subject"].unique())

if df.isnull().sum().any():
    print("ВНИМАНИЕ: есть пустые значения")
else:
    print("Данные корректны")
