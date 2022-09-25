from dash import Dash, html, dcc,Output,Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)
data = pd.read_csv('output.csv')
# data = df.groupby('date',as_index=False).sum()

app.layout = html.Div(children=[
    html.H1('PINK MORSELS SALES ANALYSIS'),
    dcc.RadioItems(
                ['north','east','south','west','all'],
                'all',
                id='region',
                inline=True
            ),
    dcc.Graph(
        id='example-graph'
    )
])

@app.callback(
    Output('example-graph','figure'),
    Input('region','value')
)
def update_graph(region_name):
    tmp = data
    if region_name!='all':
        tmp = data[data['region'] == region_name]
    fig = px.line(tmp, x="date", y="sales",title="sales per day",color='region')
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)