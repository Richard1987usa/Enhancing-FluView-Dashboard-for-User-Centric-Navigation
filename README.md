# Enhancing-FluView-Dashboard-for-User-Centric-Navigation

Project Overview:
The purpose of this project is to create an API that can access a database containing data regarding flu cases in the United States in 2023. The project uses data from multiple sources in the CDC's flu tracker and combines it into 2 tables of data: One for overall data about the entire nation and one for data divided at the state level.

Data limitations:
The following states did not report data to the CDC:
- Alaska
- Delaware
- Nevada
- New Hampshire
- Rhode Island
- Utah

Instructions:
1: Run ETL.pynb to create the Mongo database.
2: Run app.py to use the api that pulls the data from the database.
3: Ru bokeh_graphs.py to see bar graphs displaying the national and state data.

Ethical Considerations:
All of the outside sources used in the code and data are documented below. This project only uses data available from the cdc, we are not compromising people's personal health information to obtain the data.

Data Source:
https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html

The data can be obtained by clicking the green download button on the dashboard, checking both ILINet and WHO/NREVSS, selecting all seasons for NATIONAL, and selecting all seasons and regions for STATE.

week numbers for transforming the data were calculated using https://calendar.online/calendar-weeks/2023

Code sources:

Bokeh bar chart plotting: https://docs.bokeh.org/en/3.0.2/docs/user_guide/basic/bars.html

Code for Bokeh plotting with a multi-index dataframe: https://stackoverflow.com/questions/68842019/bokeh-plotting-grouped-dataframe-as-bar-chart-with-multiindex



