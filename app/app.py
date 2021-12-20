import time
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_table


from api.api import API


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# dash application
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

api=API()

def updload_files():
    """
   
    """

    return html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        accept='.zip'
    ),
    html.Div(id='output-data-upload'),
])


app.layout = updload_files






@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'))
def update_output(file):
    if file :
        print('-------------start process-------------')
        start_time = time.time()
        api.store_into_dwh(file)
        df=api.reports()
        print(f"-------------{round((time.time() - start_time)/60,2)} minutes-------------")
        return html.Div([dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        )])
    else:
        print('-------------')
        return False



if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')















# def parse_contents(contents, filename, date):
#     content_type, content_string = contents.split(',')

#     decoded = base64.b64decode(content_string)
#     try:
#         if 'csv' in filename:
#             # Assume that the user uploaded a CSV file
#             df = pd.read_csv(
#                 io.StringIO(decoded.decode('utf-8')))
#         elif 'xls' in filename:
#             # Assume that the user uploaded an excel file
#             df = pd.read_excel(io.BytesIO(decoded))
#     except Exception as e:
#         print(e)
#         return html.Div([
#             'There was an error processing this file.'
#         ])

#     return html.Div([
#         html.H5(filename),
#         html.H6(datetime.datetime.fromtimestamp(date)),

#         dash_table.DataTable(
#             data=df.to_dict('records'),
#             columns=[{'name': i, 'id': i} for i in df.columns]
#         ),

#         html.Hr(),  # horizontal line

#         # For debugging, display the raw contents provided by the web browser
#         html.Div('Raw Content'),
#         html.Pre(contents[0:200] + '...', style={
#             'whiteSpace': 'pre-wrap',
#             'wordBreak': 'break-all'
#         })
#     ])



# @app.callback(
#     Output('img', 'figure'),
#     Output('bars', 'figure'),
#     Input('class_buttons', 'value'),
#     Input('thresh', 'value'))
# def update_figure(class_, thresh):
#     """
#     callback: Receives 2 inputs.
#          Inputs: classes selected from the checkboxes and classification threshold applied. 
#          Outputs: image figure and bars figure
#     Re-render graphs based on classes checked and threshold applied 
#     Parameters
#     ----------
#     class_:list
#         list of classes checked
#     thresh:float 
#         Number between 0 and 1
#     """
#     img, bars = apply_thresh_predict(class_, thresh)

#     return img, bars


