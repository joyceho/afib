import random
from bokeh.io import curdoc
from bokeh.plotting import figure, show

x = [1,2,3,4,5]
y = [(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10)),(random.randint(1,10))]

curdoc().theme = "dark_minimal"

p = figure(title="Simple Random Graph Gen", x_axis_label="x", y_axis_label="y")

p.line(x, y, line_width=2)

show(p)