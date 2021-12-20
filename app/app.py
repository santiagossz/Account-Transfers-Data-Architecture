from dash.dependencies import Input, Output,State

from components import layouts
from components.main_dash import app
from components.callback_functions import update_output,show_upload



app.layout = layouts.set_layout()


@app.callback(Output('display-page', 'children'),
              Input('url', 'pathname'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'))
def display_page(pathname,file,filename):
    if file :
        return update_output(pathname,file,filename)            


@app.callback(Output('upload-data', 'style'),
              Input('url', 'pathname'))
def layout_desing(pathname):
    return show_upload(pathname)
        


if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
