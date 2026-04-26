import pandas as pd
import polars as pl

def load_pandas(file_path: str) -> pd.DataFrame:
    """Загружает CSV через Pandas."""
    df = pd.read_csv(file_path)
    print(f"[Pandas] Загружено строк: {df.shape[0]}, колонок: {df.shape[1]}")
    return df

def load_polars(file_path: str) -> pl.DataFrame:
    """Загружает CSV через Polars."""
    df = pl.read_csv(file_path)
    print(f"[Polars] Загружено строк: {df.shape[0]}, колонок: {df.shape[1]}")
    return df

if __name__ == "__main__":
    # тест загрузки
    df_pd = load_pandas("../data/Airline_Delay_Cause.csv")
    df_pl = load_polars("../data/Airline_Delay_Cause.csv")
    print(df_pd.head())