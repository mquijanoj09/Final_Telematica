import pandas as pd
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

fig = go.Figure(go.Densitymapbox(lat=[],lon=[],z=[],radius=20, 
opacity=0.9, zmin=0, zmax=100))
fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.4,mapbox_center_lat=6.24)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app = dash.Dash()
app.layout = html.Div([
                html.H1("Proyecto"),
                dcc.Graph(figure=fig)
                ])

app.run_server(host='0.0.0.0',port=5000)

