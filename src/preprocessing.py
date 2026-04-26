import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df['arr_flights'] > 0].copy()
    delay_cols = ['carrier_delay', 'weather_delay', 'nas_delay',
                  'security_delay', 'late_aircraft_delay']
    for col in delay_cols:
        df[col] = df[col].replace(0, np.nan)
    return df

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    # Доля задержанных рейсов
    df['delay_ratio'] = df['arr_del15'] / df['arr_flights']
    # Средняя задержка в минутах на рейс
    df['avg_delay_min'] = df['arr_delay'] / df['arr_flights']
    # Доли каждой причины от общей задержки (избегаем деления на ноль)
    cause_cols = ['carrier_delay', 'weather_delay', 'nas_delay',
                  'security_delay', 'late_aircraft_delay']
    for col in cause_cols:
        ratio_col = f'{col}_ratio'
        df[ratio_col] = df[col] / df['arr_delay'].replace(0, np.nan)
    return df

def preprocess_pandas(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df = clean_data(df)
    df = create_features(df)
    return df

if __name__ == "__main__":
    df = preprocess_pandas("../data/Airline_Delay_Cause.csv")
    print(df[['delay_ratio', 'avg_delay_min']].head())