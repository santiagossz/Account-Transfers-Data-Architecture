import base64
import io
import pandas as pd
from zipfile import ZipFile

from api.production_env.db_connection import NU_DWH

class API():

    def __init__(self,file):

        self.get_data_from_zip(file)
        self.nu_dwh=NU_DWH('nu.cod1b9wmkyuw.us-east-1.rds.amazonaws.com','nu_dwh','postgres','nu_dwh2021')

        super().__init__() 


    def get_data_from_zip(self,file):

        file_decoded = base64.b64decode(file)
        file_bytes_obj = io.BytesIO(file_decoded)
        self.file_zip = ZipFile(file_bytes_obj)
        self.file_names = self.file_zip.namelist()
       
        
    def read_data_from_zip(self,reports=True):
        self.csv_tables=[]

        for i in  self.file_names:
            if i.endswith('.txt') and not reports:
                self.schemas_script=self.file_zip.read(i).decode("utf-8")
            elif i.endswith('.csv') and not reports:
                data=self.file_zip.read(i).decode("utf-8") 
                self.csv_tables.append([i.split('/')[-2],pd.read_csv(io.StringIO(data))])
            elif i.endswith('.sql') and reports:
                self.case_sql_script=self.file_zip.read(i).decode("utf-8")
                

        
    def store_into_dwh(self):
        self.read_data_from_zip(False)
        self.nu_dwh.create_schema(self.schemas_script)
        self.nu_dwh.fetch_transformed_tables(self.csv_tables)
        self.nu_dwh.create_schema(self.schemas_script,add_relations=True)
        print('-------------schema succesfully created-------------')
        

    def reports(self,script='',amb=True):
        if amb:
            self.read_data_from_zip()
            script=self.case_sql_script
        else:
            scipt=script
        return self.nu_dwh.get_db(script)
