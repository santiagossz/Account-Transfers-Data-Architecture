from dash import dcc
from dash import html
from dash import dash_table

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
    dcc.Link('Account Monthly Balance', href='/amb'),
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
            columns=[{'name': i, 'id': i} for i in df.columns]
        )])
    
