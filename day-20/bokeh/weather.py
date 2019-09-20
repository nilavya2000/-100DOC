import pandas
 
from bokeh.plotting import figure, output_file, show
 
df=pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx",sheet_name=0)
df["Temperature"]=df["Temperature"]/10
df["Pressure"]=df["Pressure"]/10
 
p=figure(plot_width=500,plot_height=400,tools='pan')
 
p.title.text="Temperature and Air Pressure"
p.title.text_color="Gray"
p.title.text_font="arial"
p.title.text_font_style="bold"
p.xaxis.minor_tick_line_color=None
p.yaxis.minor_tick_line_color=None
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"    
 
p.circle(df["Temperature"],df["Pressure"],size=0.5)
output_file("Weather.html")
show(p)
