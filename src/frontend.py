import streamlit as st
import requests
import pandas as pd
import plotly.express as px

BACKEND_URL = "http://127.0.0.1:8000"

st.title("📊 Прогресс студентов")

# Получаем список студентов и предметов
students = requests.get(f"{BACKEND_URL}/students").json()
subjects = requests.get(f"{BACKEND_URL}/subjects").json()

student = st.selectbox("Выберите студента", students)
subject = st.selectbox("Выберите предмет", subjects)

# Получаем данные прогресса
response = requests.get(
    f"{BACKEND_URL}/progress",
    params={"student": student, "subject": subject}
)

data = response.json()

if data:
    df = pd.DataFrame(data)

    # График
    fig = px.line(
        df,
        x="date",
        y="score",
        markers=True,
        title=f"Прогресс: {student} — {subject}"
    )

    st.plotly_chart(fig)

    # Метрики
    metrics = requests.get(
        f"{BACKEND_URL}/metrics",
        params={"student": student, "subject": subject}
    ).json()

    st.subheader("📈 Метрики")
    st.write(f"Средний балл: **{metrics['average_score']}**")
    st.write(f"Тренд улучшения: **{metrics['trend']}**")

    # Экспорт
    st.subheader("⬇ Экспорт данных")
    st.download_button(
        "Скачать CSV",
        df.to_csv(index=False),
        file_name="progress.csv",
        mime="text/csv"
    )
else:
    st.warning("Нет данных")
