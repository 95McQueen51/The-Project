import pandas as pd

df = pd.read_csv("data.csv")

report = df.groupby(["student", "subject"])["score"].mean()

with open("report.txt", "w", encoding="utf-8") as f:
    f.write("Средний балл по студентам\n\n")
    f.write(report.to_string())

print("Отчет сохранен в report.txt")
