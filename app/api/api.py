import base64
import io
import pandas as pd
from zipfile import ZipFile

from api.production_env.db_connection import NU_DWH

class API():

    def __init__(self):
        self.csv_tables=[]
        self.nu_dwh=NU_DWH('localhost','nu_dwh','postgres','Tumarnamki55')


        super().__init__() 

    def extract_data_from_zip(self,file):
        file_decoded = base64.b64decode(file)
        file_bytes_obj = io.BytesIO(file_decoded)
        file_zip = ZipFile(file_bytes_obj)
        file_names = file_zip.namelist()
       
        for i in file_names:
            if i.endswith('.txt'):
                self.schemas_script=file_zip.read(i).decode("utf-8")
            elif i.endswith('.sql'):
                self.case_sql_script=file_zip.read(i).decode("utf-8")
            elif i.endswith('.csv'):
                data=file_zip.read(i).decode("utf-8") 
                self.csv_tables.append([i.split('/')[-2],pd.read_csv(io.StringIO(data))])
                

        
    def store_into_dwh(self,file):
        self.extract_data_from_zip(file)
        self.nu_dwh.create_schema(self.schemas_script)
        self.nu_dwh.fetch_transformed_tables(self.csv_tables)
        self.nu_dwh.create_schema(self.schemas_script,add_relations=True)
        print('-------------schema succesfully created-------------')
        

    def reports(self):
        return self.nu_dwh.get_db(self.case_sql_script)
