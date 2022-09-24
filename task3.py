from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('output.csv')
data = df.groupby('date',as_index=False).sum()
fig = px.line(data, x="date", y="sales",title="sales per day")
app.layout = html.Div(children=[
    html.H1('PINK MORSELS SALES ANALYSIS'),
    dcc.RadioItems(
                ['north','east','south','west','all'],
                'all',
                id='xaxis-type',
                inline=True
            ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)