import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def fetch_covid_data():
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    try:
        data = pd.read_csv(url)
        return data
    except Exception as e:
        print(f"Failed to fetch COVID-19 data: {e}")
        return None

def process_covid_data(data, country):
    if data is None:
        return None

    country_data = data[data['Country/Region'] == country].iloc[:, 4:].T

    country_data.columns = ['Cases']

    country_data.index = pd.to_datetime(country_data.index)

    return country_data

def millions_formatter(x, pos):
    return f"{x/1e6:.1f}M"

def visualize_covid_data(country_data, country):
    if country_data is None:
        return

    plt.figure(figsize=(12, 6))
    plt.plot(country_data.index, country_data['Cases'], label=f"Total Cases in {country}", color="blue")

    plt.title(f"COVID-19 Total Cases in {country}")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases (Millions)")
    plt.legend()
    plt.grid(True)
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    plt.tight_layout()

    plt.show()

def main():
    covid_data = fetch_covid_data()
    if covid_data is not None:
        print("Available countries:")
        print(", ".join(covid_data['Country/Region'].unique()))
        country = input("Enter the country name (e.g., US, India): ")
        country_data = process_covid_data(covid_data, country)
        visualize_covid_data(country_data, country)

if __name__ == "__main__":
    main()
