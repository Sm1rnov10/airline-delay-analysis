import os
import sys
from src.analysis import monthly_carrier_summary, airport_delay_ranking, cause_breakdown
from src.benchmark import run_benchmark
from src.preprocessing import preprocess_pandas
from src.visualization import run_all_visualizations

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "Airline_Delay_Cause.csv")


def main():
    print("=" * 60)
    print("Анализ задержек авиарейсов США, 2022")
    print("=" * 60)

    print("\n[1] Загружаем и очищаем данные...")
    df = preprocess_pandas(DATA_PATH)
    print(f"   Данные готовы: {df.shape[0]} записей, {df.shape[1]} колонок.")

    # 2. Аналитические сводки
    print("\n[2] Аналитические таблицы:")
    monthly = monthly_carrier_summary(df)
    print("   - Месячная динамика (первые 5 строк):")
    print(monthly.head())

    top_airports = airport_delay_ranking(df)
    print("\n   - Топ-10 аэропортов по средней задержке:")
    print(top_airports)

    causes = cause_breakdown(df)
    print("\n   - Общее количество минут задержек по причинам:")
    print(causes)

    print("\n[3] Генерация графиков...")
    run_all_visualizations(df)

    print("\n[4] Сравнение Pandas и Polars:")
    run_benchmark(DATA_PATH)

    print("\nАнализ завершён. Результаты сохранены в папку reports/")
    print("   Статические графики: reports/static/")
    print("   Интерактивные графики: reports/interactive/ (откройте HTML в браузере)")


if __name__ == "__main__":
    main()