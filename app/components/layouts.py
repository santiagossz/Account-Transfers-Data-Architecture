from dash import dcc
from dash import html
from dash import dash_table
from dash.html.Div import Div

from .metrics_functions import total_status,transaction_status

def set_layout():
    return html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        accept='.zip',
     
    ),
    html.Br(),
    dcc.Link('Account Monthly Balance', href='/account-monthly-balance'),
    html.Br(),
    dcc.Link('PIX Metrics', href='/pix-metrics'),
    html.Br(),
    html.Div(id='display-page')

])

def index_layout(filename):
    return html.Div([
                html.H6(filename)
                ])

def amb_layout(df):

    return html.Div([dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i, 'type':'text' if i=='full_name' else 'numeric'} for i in df.columns],
            filter_action='native',
            sort_action='native'
            
        )])
    
def pix_layout(df):
    pie_status=total_status(df)
    bar_status=transaction_status(df)
    return html.Div([
            html.H6('PIX Transaction status Metrics 2020'),
            
            html.Div([
            dcc.Graph(figure=pie_status),
            dcc.Graph(figure=bar_status)],
            style={'display': 'flex  '})]
            ,style={'textAlign':'center'}
        )