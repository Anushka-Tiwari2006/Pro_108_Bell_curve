import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("data.csv")
Avg_rate = df["Avg_Rating"].to_list()
colors = ['purple']
fig = ff.create_distplot([Avg_rate],["Average Rating"],colors=colors)
fig.show()