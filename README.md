# Анализ задержек авиарейсов 

## Данные
- **Источник:** Bureau of Transportation Statistics (BTS), датасет `Airline Delay Cause`.
- **Содержание:** помесячная статистика задержек по авиакомпаниям и аэропортам США за 2022 год.
- **Ключевые поля:**  
  `arr_flights`, `arr_del15`, `carrier_delay`, `weather_delay`, `nas_delay`, `late_aircraft_delay` и др.

## Используемые технологии

- Python 3.14
- Pandas, Polars – обработка данных
- Seaborn, Matplotlib – статические графики
- Plotly – интерактивные дашборды
- NumPy

## Структура проекта
```
airline-delay-analysis/
├── data/
│   └── Airline_Delay_Cause.csv
├── src/
│   ├── __init__.py
│   ├── preprocessing.py       # очистка
│   ├── analysis.py            # сводные таблицы (аэропорты, авиакомпании, причины)
│   ├── visualization.py       # статические и интерактивные графики
│   ├── benchmark.py           # сравнение Pandas и Polars
│   └── main.py                # запуск всех этапов
├── reports/
│   ├── static/                # PNG-графики (Seaborn)
│   └── interactive/           # HTML-дашборды (Plotly)
├── requirements.txt
└── README.md
```
## Запуск

1. **Клонируйте репозиторий**
2. **Поместите файл данных** `Airline_Delay_Cause.csv` в папку `data/`.
3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
4. **Запустите проект**
   ```bash
   python src/main.py
