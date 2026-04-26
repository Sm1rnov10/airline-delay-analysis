import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

STATIC_DIR = "../reports/static"
INTERACTIVE_DIR = "../reports/interactive"
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(INTERACTIVE_DIR, exist_ok=True)

def plot_delay_distribution(df: pd.DataFrame):
    plt.figure(figsize=(10,5))
    data = df[df['avg_delay_min'] <= 300]  # без выбросов
    sns.histplot(data['avg_delay_min'], bins=50, kde=True)
    plt.title('Distribution of average arrival delay per route')
    plt.xlabel('Average delay (minutes)')
    plt.savefig(f"{STATIC_DIR}/delay_distribution.png", dpi=150)
    plt.close()

def plot_delay_by_airline(df: pd.DataFrame):
    top = df.groupby('carrier_name')['arr_flights'].sum().nlargest(10).index
    df_top = df[df['carrier_name'].isin(top)]
    plt.figure(figsize=(12,6))
    sns.boxplot(data=df_top, x='carrier_name', y='avg_delay_min')
    plt.xticks(rotation=45)
    plt.title('Delay distribution by major airlines')
    plt.tight_layout()
    plt.savefig(f"{STATIC_DIR}/delay_by_airline.png", dpi=150)
    plt.close()

def plot_correlation_heatmap(df: pd.DataFrame):
    cause_ratio_cols = ['carrier_delay_ratio', 'weather_delay_ratio',
                        'nas_delay_ratio', 'late_aircraft_delay_ratio']
    corr = df[cause_ratio_cols].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation between delay cause ratios')
    plt.tight_layout()
    plt.savefig(f"{STATIC_DIR}/correlation_heatmap.png", dpi=150)
    plt.close()

def plot_monthly_trend(df: pd.DataFrame):
    monthly = df.groupby('month')['delay_ratio'].mean().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(data=monthly, x='month', y='delay_ratio', marker='o')
    plt.title('Average delay ratio by month')
    plt.xticks(range(1,13))
    plt.ylabel('Proportion of delayed flights')
    plt.savefig(f"{STATIC_DIR}/monthly_trend.png", dpi=150)
    plt.close()

def interactive_delay_timeline(df: pd.DataFrame):
    monthly = df.groupby(['month', 'carrier_name'])['delay_ratio'].mean().reset_index()
    fig = px.line(monthly, x='month', y='delay_ratio', color='carrier_name',
                  title='Monthly delay ratio by airline',
                  labels={'delay_ratio': 'Proportion delayed', 'month': 'Month'})
    fig.update_layout(legend_title_text='Airline', legend=dict(itemsizing='constant'))
    fig.write_html(f"{INTERACTIVE_DIR}/delay_timeline.html")
    return fig

def interactive_cause_stack(df: pd.DataFrame):
    top_airports = df.groupby('airport_name')['arr_flights'].sum().nlargest(5).index
    df_top = df[df['airport_name'].isin(top_airports)]
    cause_sum = df_top.groupby('airport_name')[['carrier_delay', 'weather_delay',
                                                'nas_delay', 'security_delay',
                                                'late_aircraft_delay']].sum().reset_index()
    cause_melted = cause_sum.melt(id_vars='airport_name', var_name='delay_type', value_name='total_minutes')
    fig = px.bar(cause_melted, x='airport_name', y='total_minutes', color='delay_type',
                 title='Delay causes at busiest airports', barmode='stack')
    fig.write_html(f"{INTERACTIVE_DIR}/cause_stack.html")
    return fig

def run_all_visualizations(df: pd.DataFrame):
    print("Строим статические графики (Seaborn)...")
    plot_delay_distribution(df)
    plot_delay_by_airline(df)
    plot_correlation_heatmap(df)
    plot_monthly_trend(df)
    print("Статические графики сохранены в reports/static/")

    print("Строим интерактивные графики (Plotly)...")
    interactive_delay_timeline(df)
    interactive_cause_stack(df)
    print("Интерактивные графики сохранены в reports/interactive/")

if __name__ == "__main__":
    from preprocessing import preprocess_pandas
    df = preprocess_pandas("../data/Airline_Delay_Cause.csv")
    run_all_visualizations(df)