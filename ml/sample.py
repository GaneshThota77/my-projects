import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_covid_data(country):
    url = f'https://api.covid19api.com/dayone/country/{country}/status/confirmed/live'
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

def plot_covid_data(df, country):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Cases'], label=f'Daily New Cases in {country}', marker='o', linestyle='-')
    plt.title(f'Daily New COVID-19 Cases in {country}')
    plt.xlabel('Date')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    country_name = 'YourCountry'  # Replace with the name of the country you're interested in
    covid_data = fetch_covid_data(country_name)
    plot_covid_data(covid_data, country_name)
