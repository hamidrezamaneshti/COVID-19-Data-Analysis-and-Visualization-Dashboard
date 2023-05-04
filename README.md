# COVID-19-Data-Analysis-and-Visualization-Dashboard
This is a dashboard that allows users to explore COVID-19 data in different ways, including selecting a country or region, a date range, and a type of data, and displaying the corresponding charts and tables.

## Getting Started

### Prerequisites
To run this dashboard, you will need:

* Python 3.6 or higher
* Pandas, Numpy, Plotly, Dash libraries
* COVID-19 dataset

### Installation

1. Clone the repository to your local machine:
`git clone https://github.com/hamidrezamaneshti/COVID-19-dashboard.git`
2. Install the necessary libraries:
`pip install pandas numpy plotly dash`
3. Download the COVID-19 dataset from "https://api.covid19api.com/summary" or ([WHO](https://covid19.who.int/WHO-COVID-19-global-data.csv) / [John Hopkins University](https://github.com/CSSEGISandData/COVID-19).)
4. Move the dataset to the data directory.

### Usage

1. Navigate to the root directory of the project.
2. Run the following command:
`python mian.py #For getting, cleaning, analyzing data`
`python app.py #Run Dashboard`
`python visualization.py #For generating plots(Optional)`
3. Open your browser and go to http://localhost:8050/.
4. Select a country or region, a date range, and a type of data, and the dashboard will display the corresponding charts and tables.

## Screen Shots
These figures are samples of visualizations.
![](https://s8.uupload.ir/files/1_6qe8.jpg)
![](https://s8.uupload.ir/files/2_kfio.jpg)
![](https://s8.uupload.ir/files/3_4vsh.jpg)

Figure below is screen shot of dashboard runs on browser.
![](https://s8.uupload.ir/files/4_u14f.jpg)

## Replicating the Analysis

If you would like to replicate the analysis and create your own dashboard, you can follow these steps:

1. Collect COVID-19 data from reliable sources such as World Health Organization, Centers for Disease Control and Prevention, or John Hopkins University. Store the data in a CSV or Excel file for easy manipulation using Python.

2. Use Python's Pandas library to clean and transform the data as needed. For example, you may need to remove duplicates, handle missing data, or reformat dates.

3. Use Pandas and Numpy libraries to perform exploratory data analysis and derive insights from the data. For example, you could calculate the total number of cases, deaths, and recoveries for each country or region, or calculate the daily growth rate of cases.

4. Once you've calculated the necessary metrics, you can use them to derive insights from the data. For example, you could create a bar chart to compare the total number of cases, deaths, and recoveries for each country, or create a line chart to visualize the daily growth rate of cases over time.

5. Use Python's Dash or Flask libraries to create an interactive dashboard that allows users to explore the data in different ways. The dashboard should allow users to select a country or region, a date range, and a type of data, and display the corresponding charts and tables.

## Acknowledgments

[WHO](https://covid19.who.int/)
[John Hopkins University](https://github.com/CSSEGISandData/COVID-19)

