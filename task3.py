from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('output.csv')
data = df.groupby('date',as_index=False).sum()
fig = px.bar(data, x="date", y="sales",title="sales per day")
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)