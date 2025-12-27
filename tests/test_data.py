import pandas as pd

def test_data_file_exists():
    df = pd.read_csv("data/sample.csv")
    assert not df.empty


def test_required_columns():
    df = pd.read_csv("data/sample.csv")
    required_columns = {"student", "subject", "date", "score"}
    assert required_columns.issubset(df.columns)
