import pandas as pd

def monthly_carrier_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby(['year', 'month', 'carrier_name']).agg(
        total_flights=('arr_flights', 'sum'),
        total_delayed=('arr_del15', 'sum'),
        total_delay_min=('arr_delay', 'sum'),
        avg_delay_ratio=('delay_ratio', 'mean'),
        avg_delay_per_flight=('avg_delay_min', 'mean')
    ).reset_index()
    summary['delay_rate'] = summary['total_delayed'] / summary['total_flights']
    return summary

def airport_delay_ranking(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    airport_stats = df.groupby('airport_name').agg(
        total_flights=('arr_flights', 'sum'),
        avg_delay=('avg_delay_min', 'mean')
    ).reset_index()
    airport_stats = airport_stats[airport_stats['total_flights'] > 100]
    airport_stats = airport_stats.sort_values('avg_delay', ascending=False).head(top_n)
    return airport_stats

def cause_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    causes = ['carrier_delay', 'weather_delay', 'nas_delay',
              'security_delay', 'late_aircraft_delay']
    total = df[causes].sum().reset_index()
    total.columns = ['delay_cause', 'total_minutes']
    return total.sort_values('total_minutes', ascending=False)

if __name__ == "__main__":
    from preprocessing import preprocess_pandas
    df = preprocess_pandas("../data/Airline_Delay_Cause.csv")
    print(monthly_carrier_summary(df).head())
    print(airport_delay_ranking(df))
    print(cause_breakdown(df))