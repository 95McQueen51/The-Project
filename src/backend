from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Загружаем данные
data = pd.read_csv("../data.csv", parse_dates=["date"])

@app.get("/students")
def get_students():
    return sorted(data["student"].unique().tolist())

@app.get("/subjects")
def get_subjects():
    return sorted(data["subject"].unique().tolist())

@app.get("/progress")
def get_progress(student: str, subject: str):
    df = data[(data["student"] == student) & (data["subject"] == subject)]
    return df.to_dict(orient="records")

@app.get("/metrics")
def get_metrics(student: str, subject: str):
    df = data[(data["student"] == student) & (data["subject"] == subject)]

    if df.empty:
        return {}

    avg_score = round(df["score"].mean(), 2)
    trend = df["score"].iloc[-1] - df["score"].iloc[0]

    return {
        "average_score": avg_score,
        "trend": trend
    }
