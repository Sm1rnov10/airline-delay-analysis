import time
import pandas as pd
import polars as pl


def benchmark_pandas(file_path: str):
    df = pd.read_csv(file_path)
    start = time.time()
    result = df.groupby(['carrier', 'month']).agg(
        median_delay=('arr_delay', 'median'),
        total_flights=('arr_flights', 'sum')
    ).reset_index()
    result = result[result['total_flights'] > 100]
    elapsed = time.time() - start
    return elapsed, result.shape


def benchmark_polars(file_path: str):
    df = pl.scan_csv(file_path)
    start = time.time()
    result = (df.group_by(['carrier', 'month'])
              .agg([
        pl.median('arr_delay').alias('median_delay'),
        pl.sum('arr_flights').alias('total_flights')
    ])
              .filter(pl.col('total_flights') > 100)
              .collect()
              )
    elapsed = time.time() - start
    return elapsed, result.shape


def run_benchmark(file_path: str):
    print("=== Бенчмарк Pandas vs Polars ===")
    print("Запрос: группировка по carrier, month -> медиана задержки, сумма рейсов; фильтр >100 рейсов.")

    time_pd, shape_pd = benchmark_pandas(file_path)
    print(f"Pandas: {time_pd:.4f} сек, результат {shape_pd}")

    time_pl, shape_pl = benchmark_polars(file_path)
    print(f"Polars: {time_pl:.4f} сек, результат {shape_pl}")

    speedup = time_pd / time_pl if time_pl > 0 else float('inf')
    print(f"Polars быстрее в {speedup:.2f} раза")


if __name__ == "__main__":
    run_benchmark("../data/Airline_Delay_Cause.csv")