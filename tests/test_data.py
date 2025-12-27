import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sample.csv"


def test_data_file_exists():
    assert DATA_FILE.exists()
    df = pd.read_csv(DATA_FILE)
    assert not df.empty


def test_required_columns():
    df = pd.read_csv(DATA_FILE)
    required_columns = {"student", "subject", "date", "score"}
    assert required_columns.issubset(df.columns)
