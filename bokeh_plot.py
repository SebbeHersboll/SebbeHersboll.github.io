# bokeh_plot.py

from bokeh.plotting import figure, output_file, save

# Create some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Output to static HTML file
output_file("bokeh_plot.html")

# Create a new plot
p = figure(title="Simple Bokeh Plot", x_axis_label='x', y_axis_label='y')

# Add a line renderer with circle markers
p.line(x, y, legend_label="Temp.", line_width=2)
p.scatter(x, y, legend_label="Temp.", fill_color="white", size=8)

# Save the plot
save(p)
