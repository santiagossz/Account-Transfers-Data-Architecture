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
    dcc.Link('PIX Metrics', href='/aa'),
    html.Br(),
    html.Div(id='display-page')

])

def index_layout(filename):
    return html.Div([
                html.H6(filename)
                ])

def amb_layout(df):
    # df['month_number']=df['month_number'].astype(int)

    return html.Div([dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i, 'type':'text' if i=='full_name' else 'numeric'} for i in df.columns],
            filter_action='native',
            sort_action='native'
            
        )])
    
