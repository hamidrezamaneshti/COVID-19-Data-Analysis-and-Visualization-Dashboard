import pandas as pd
import requests


def getting_dataset():
    # Define the URL of the API endpoint
    url = "https://api.covid19api.com/summary"
    # Send a GET request to the API endpoint
    response = requests.get(url)
    # Convert the response to a JSON object
    data = response.json()
    # Convert the JSON object to a pandas DataFrame
    df = pd.DataFrame(data["Countries"])
    # Save the DataFrame to a CSV file
    df.to_csv("covid_data.csv", index=False)


def data_cleaning():
    # Read RAW data
    df = pd.read_csv("covid_data.csv")
    # Check for missing data
    print(df.isnull().sum())
    # Drop missed (if there is unimportant data)
    df = df.dropna()
    # Show duplicated data
    duplicated = (df.duplicated().sum())
    print("Duplicated: ", duplicated)
    if duplicated >= 1:
        df = df.drop_duplicates()
    else:
        pass
    # change the time format
    df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%d/%m/%Y")
    # Save the cleaned data
    df.to_csv("cleaned_covid_data.csv", index=False)


def data_analysis():
    df = pd.read_csv("cleaned_covid_data.csv")

    grouped_data = df.groupby("Country")
    total_cases = grouped_data["TotalConfirmed"].sum()
    total_deaths = grouped_data["TotalDeaths"].sum()
    total_recoveries = grouped_data["TotalRecovered"].sum()

    daily_cases = df.groupby(["Country", "Date"])["NewConfirmed"].sum().reset_index()

    analyzed_data = pd.DataFrame(
        {"TotalConfirmed": total_cases, "TotalDeaths": total_deaths, "TotalRecovered": total_recoveries,
         "Country": total_cases.index})
    date_data = pd.DataFrame({"Country": daily_cases["Country"], "Date": pd.to_datetime(daily_cases["Date"])})
    analyzed_data = analyzed_data.reset_index(drop=True)
    analyzed_data = analyzed_data.merge(date_data, on="Country")

    analyzed_data.to_csv("analyzed_covid_data.csv", index=False)


if __name__ == '__main__':
    getting_dataset()
    data_cleaning()
    data_analysis()
    data_analysis()