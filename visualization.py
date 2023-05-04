import matplotlib.pyplot as plt
import pandas as pd


def total_confirmed_plt(analyzed_data):
    N = 10
    top_countries = analyzed_data.nlargest(N, "TotalConfirmed")
    top_countries.plot(kind="bar", y="TotalConfirmed", figsize=(12, 8))
    plt.title(f"COVID-19 Cases: Top {N} Countries")
    plt.xlabel("Country")
    plt.ylabel("Number of Cases")
    plt.show()


def cases_plt(analyzed_data):
    analyzed_data.plot(kind="hist", bins=10, alpha=0.5, figsize=(12, 8))
    plt.title("COVID-19 Cases by Country Over Time")
    plt.xlabel("Number of Cases")
    plt.ylabel("Frequency")
    plt.show()


def top10_country_plt(analyzed_data):
    # Get the top 10 countries by TotalConfirmed cases
    top_10_confirmed = analyzed_data.sort_values(by='TotalConfirmed', ascending=False)[:10]
    # Get the top 10 countries by TotalDeaths
    top_10_deaths = analyzed_data.sort_values(by='TotalDeaths', ascending=False)[:10]
    # Get the top 10 countries by TotalRecovered
    top_10_recovered = analyzed_data.sort_values(by='TotalRecovered', ascending=False)[:10]
    # Combine the top 10 countries by TotalConfirmed, TotalDeaths, and TotalRecovered
    top_10 = pd.concat([top_10_confirmed, top_10_deaths, top_10_recovered]).drop_duplicates()
    # Plot the bar chart for the top 10 countries
    top_10.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title("COVID-19 Cases by Top 10 Countries")
    plt.xlabel("Country")
    plt.ylabel("Number of Cases")
    plt.show()


if __name__ == '__main__':
    analyzed_data = pd.read_csv("analyzed_covid_data.csv", index_col="Country")
    total_confirmed_plt(analyzed_data)
    cases_plt(analyzed_data)
    top10_country_plt(analyzed_data)
