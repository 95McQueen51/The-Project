import pandas as pd


def test_empty_dataframe():
    df = pd.DataFrame(columns=["student", "subject", "date", "score"])
    assert df.empty
