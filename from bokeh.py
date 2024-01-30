# Import the required packages
from bokeh.io import output_file, show
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral5
from bokeh.sampledata.autompg import autompg as df
from bokeh.transform import factor_cmap
# from bokeh.palettes import viridis

from bokeh.layouts import row
import pandas as pd

# Create two data frames from the imported tables
import csv
# df1 = pd.read_csv('combined_state_data.csv')
# df2 = pd.read_csv('combined_national_data.csv')

# Create two data sources from the data frames
# source1 = ColumnDataSource(df1)
# source2 = ColumnDataSource(df2)

# Determine where the visualization will be rendered
output_file('my_bokeh_plot.html')
colors = ["red","blue","green","purple","yellow","orange"]

# Set up the figures
df = pd.read_csv('combined_state_data.csv')
# colors = (len(df['REGION'].tolist()))
p=figure(x_range=df['REGION'],title="State Data", height=400, width=800)
p.vbar(x=df["REGION"], top = df["PERCENT POSITIVE"],width=0.9, color=colors)
show(p)
# fig1 = figure(title='State Data', width=400, height=400)
# fig2 = figure(title='National Data', width=600, height=300)

# Connect to and draw the data
# fig1.vbar(x_range=source1, color='blue', height=250, legend_label='State Data')
# fig2.vbar(source=source2, color='green', alpha=0.8, legend_label='National Data')

# Organize the layout
# layout = row(fig1)

# Preview and save the visualization
# show(layout)
