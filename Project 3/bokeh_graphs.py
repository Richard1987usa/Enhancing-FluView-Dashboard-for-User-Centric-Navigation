import pandas as pd
from bokeh.models.layouts import Column
from bokeh.models  import ColumnDataSource, FactorRange
from bokeh.plotting import figure, show

df = pd.read_csv('combined_national_data.csv')
df2 = pd.read_csv('combined_state_data.csv')

#bar chart code from
#https://docs.bokeh.org/en/3.0.2/docs/user_guide/basic/bars.html

month = list(df['MONTH'])
counts = list(df['PERCENT POSITIVE'])

p1 = figure(x_range=month, height=350, title="Percent of Flu Test Positives by Month Nationally",
           toolbar_location=None, tools="")

p1.vbar(x=month, top=counts, width=0.9)

p1.xgrid.grid_line_color = None
p1.y_range.start = 0

#Plotting Bokeh multi index
#https://stackoverflow.com/questions/68842019/bokeh-plotting-grouped-dataframe-as-bar-chart-with-multiindex
grouped = pd.DataFrame(df2.groupby(['REGION', 'MONTH'])[['PERCENT POSITIVE']].sum())
states = list(df2['REGION'])
months = list(df2['MONTH'])
grouped['group'] = [''.join(str(x)) for x in grouped.index]
source = ColumnDataSource(data=grouped)


p2 = figure(x_range=FactorRange(*source.data['group'].tolist()), width = 5000, height = 500)
p2.vbar(x='group', top='PERCENT POSITIVE', source=source, width = 0.5)
p2.xaxis.major_label_orientation = "vertical"

p = Column(p1, p2)
show(p)
