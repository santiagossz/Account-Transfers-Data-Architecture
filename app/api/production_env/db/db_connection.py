import psycopg2
import pandas as pd
from .db_tables import DWH_TABLES
from sqlalchemy import create_engine
from .db_etl import ETL


class NU_DWH(DWH_TABLES,ETL):
    def __init__(self, host,dbname,user,password):

        super().__init__() 

        self.host=host
        self.dbname=dbname
        self.user=user
        self.password=password

        self.conn=psycopg2.connect(f' host={self.host} dbname={self.dbname} user={self.user} password={self.password}')
        self.conn.autocommit=True

        
    def execute_sql(self,script):
        cur=self.conn.cursor()
        cur.execute(script)
        cur.close()  

            
    def create_schema(self,files,add_relations=False):
        self.add_relations=add_relations
        self.create_tables(files)
        self.execute_sql(self.script)

 
    def fetch_data(self,sql_table,df):
        engine = create_engine(f'postgresql://{self.user}:{self.password}@{self.host}/{self.dbname}')
        if not pd.read_sql(f'SELECT COUNT(*) FROM {sql_table}', self.conn)['count'][0]:
            df.to_sql(sql_table,engine,index=False, if_exists='append')

    
    def get_db(self,sql):
        return  pd.read_sql(sql, self.conn)

    # def close_db_connection(self):
    #     close_script=f""""
    #     SELECT 
    #     pg_terminate_backend(procpid) 
    #     FROM 
    #         pg_stat_activity 
    #     WHERE 
    #     -- don't kill my own connection!
    #     procpid <> pg_backend_pid()
    #     -- don't kill the connections to other databases
    #     AND datname = {self.dbname};
    #     """
    #     self.execute_sql(close_script)
        


       
       
            

