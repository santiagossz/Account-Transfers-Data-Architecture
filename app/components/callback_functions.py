import time
from api.api import API
from components import layouts 
import api.reporting_env.reporting as rp

def update_output(pathname, file, filename):
    start_time = time.time()
    print('-------------start process-------------')
    api = API(file)
    if pathname == '/':
        # api.store_into_dwh()
        print(
            f"-------------{round((time.time() - start_time)/60,2)} minutes to create the schema-------------")
        return layouts.index_layout(filename)
    elif pathname == '/account-monthly-balance':
        df = api.reports()
        print(
            f"-------------{round((time.time() - start_time)/60,2)} minutes  to create the account monthly balance report-------------")        
        return layouts.amb_layout(df)
    elif pathname=='/pix-metrics':
        pix_df = api.reports(rp.pix,False)
        failed_tr_df=api.reports(rp.failed_tr,False)

        return layouts.pix_layout(pix_df,failed_tr_df)



def show_upload(pathname):
    if pathname == '/':
        return {
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
        }
    else:
        return {
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
        }
        # return {'display': 'none'}
