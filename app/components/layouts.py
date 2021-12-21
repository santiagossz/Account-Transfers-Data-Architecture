from dash import dcc
from dash import html
from dash import dash_table
from dash.html.Div import Div

from .metrics_functions import plot_status,plot_comparisson

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
    
def pix_layout(pix_df,failed_tr_df):
    status=plot_status(pix_df,failed_tr_df)
    comparisson=plot_comparisson(pix_df,failed_tr_df)
    return html.Div([
            html.Div([
            dcc.Graph(figure=status)],
            style={'display': 'flex  '}),
             html.Div([
            html.Div([dcc.Graph(figure=comparisson)])
            # ,html.Div([dcc.Graph(figure=comparisson[1])])
            ]
            )
            ],
            style={'display': 'flex  '} )