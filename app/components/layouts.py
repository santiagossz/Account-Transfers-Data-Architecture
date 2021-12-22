from math import pi
from dash import dcc
from dash import html
from dash import dash_table
from dash.html.Div import Div

from .metrics_functions import status_comp,failed_transfers,growth_week,pix_states

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
    dcc.Link('Upload Files', href='/'),
    html.Br(),
    dcc.Link('Account Monthly Balance', href='/account-monthly-balance'),
    html.Br(),
    dcc.Link('PIX Metrics', href='/pix-metrics'),
    html.Br(),
    html.Div(id='display-page')

])

def index_layout(filename):
    return html.Div([
                html.H6(f'File: {filename} uploaded sucessfully')
                ])

def amb_layout(df):

    return html.Div([dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i, 'type':'text' if i=='full_name' else 'numeric'} for i in df.columns],
            filter_action='native',
            sort_action='native'
            
        )])
    
def pix_layout(pix_df,tr_df):
    status=status_comp(pix_df,tr_df)
    failed=failed_transfers(pix_df)
    weeks=growth_week(pix_df)
    states=pix_states(pix_df)
    return html.Div([
            html.Div([
            dcc.Graph(figure=status),
            dcc.Graph(figure=failed)],
            style={'display': 'flex','testAlign':'center'}),
             
            html.Div([
               dcc.Graph(figure=weeks)
            ]),
             html.Div([
               dcc.Graph(figure=states)
            ])
            ],
            style={'display': 'flex-inline'} )