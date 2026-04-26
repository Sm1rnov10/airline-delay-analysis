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
airline-delay-analysis/
├── data/ # сюда положить CSV-файл
├── src/ # исходный код
│ ├── preprocessing.py # очистка, создание признаков
│ ├── analysis.py # агрегации и группировки
│ ├── visualization.py # все графики
│ ├── benchmark.py # сравнение Pandas vs Polars
│ └── main.py # запуск всего анализа
├── reports/ # результаты (создаётся автоматически)
│ ├── static/ # PNG-графики Seaborn
│ └── interactive/ # HTML-дашборды Plotly
├── requirements.txt
└── README.md

## Запуск

1. **Клонируйте репозиторий**
2. **Поместите файл данных** `Airline_Delay_Cause.csv` в папку `data/`.
3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
4. **Запустите проект**
   ```bash
   python src/main.py
