import pandas as pd


def calculate_metrics(df):
    avg = df["score"].mean()
    trend = df["score"].iloc[-1] - df["score"].iloc[0]
    return avg, trend


def test_metrics_calculation():
    data = {
        "score": [70, 80, 90]
    }
    df = pd.DataFrame(data)

    avg, trend = calculate_metrics(df)

    assert avg == 80
    assert trend == 20
