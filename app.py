import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# Load the cleaned and analyzed data
analyzed_data = pd.read_csv("analyzed_covid_data.csv")

# Group the data by country and sum the cases
total_cases = analyzed_data.groupby("Country")[["TotalConfirmed", "TotalDeaths", "TotalRecovered"]].sum().reset_index()

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([

    # Create a dropdown menu for selecting the country
    html.Label("Select a country:"),
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country, "value": country} for country in total_cases["Country"]],
        value="US"
    ),

    # Create a date range picker for selecting the date range
    html.Label("Select a date range:"),
    dcc.DatePickerRange(
        id="date-range-picker",
        min_date_allowed=analyzed_data["Date"].min(),
        max_date_allowed=analyzed_data["Date"].max(),
        start_date=analyzed_data["Date"].min(),
        end_date=analyzed_data["Date"].max()
    ),

    # Create a radio button for selecting the type of data
    html.Label("Select the type of data:"),
    dcc.RadioItems(
        id="data-type-radio",
        options=[
            {"label": "Total cases", "value": "TotalConfirmed"},
            {"label": "Total deaths", "value": "TotalDeaths"},
            {"label": "Total recoveries", "value": "TotalRecovered"}
        ],
        value="TotalConfirmed"
    ),

    # Create a bar chart of the selected data
    dcc.Graph(id="bar-chart"),

    # Create a table of the selected data
    html.Table(id="table")
])


# Define the callbacks for the app
@app.callback(
    [Output("bar-chart", "figure"), Output("table", "children")],
    [Input("country-dropdown", "value"), Input("date-range-picker", "start_date"),
     Input("date-range-picker", "end_date"), Input("data-type-radio", "value")]
)
def update_data(country, start_date, end_date, data_type):
    # Filter the data based on the user's selections
    filtered_data = analyzed_data[(analyzed_data["Country"] == country) & (analyzed_data["Date"] >= start_date) & (
            analyzed_data["Date"] <= end_date)]

    # Group the data by date and sum the cases
    grouped_data = filtered_data.groupby("Date")[data_type].sum().reset_index()

    # Create the bar chart
    bar_chart = px.bar(grouped_data, x="Date", y=data_type, title=f"{data_type} in {country}")

    # Create the table
    table = html.Table([
        html.Tr([html.Th("Date"), html.Th(data_type)]),
        *[html.Tr([html.Td(date), html.Td(value)]) for date, value in
          zip(grouped_data["Date"], grouped_data[data_type])]
    ])

    return bar_chart, table


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
