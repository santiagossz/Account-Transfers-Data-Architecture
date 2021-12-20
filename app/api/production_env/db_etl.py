import pandas as pd


class ETL():

    def __init__(self):
        super().__init__()

    def fetch_transformed_tables(self, csv_tables):
        no_sql_dwh = {t[0]: {'sql_table': t[0],
                             'df': self.order_columns_df(t[1], t[0]),
                             'uuid_columns': self.uuid_columns(t[0])} for t in csv_tables}

        tables_name_data = [
            [i['sql_table'], self.formatted_df(i)] for i in no_sql_dwh.values()]

        [self.fetch_data(i[0], i[1]) for i in tables_name_data]

    def order_columns_df(self, df, sql_table):
        return df.reindex(columns=self.get_db(f'SELECT * FROM {sql_table} LIMIT 1').columns)

    def uuid_columns(self, sql_table):
        return self.get_db(f"""SELECT COLUMN_NAME
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE  TABLE_NAME = '{sql_table}' AND DATA_TYPE='uuid'""")['column_name'].values

    def formatted_df(self, db):
        for i in db['uuid_columns']:
            db['df'][i] = db['df'][i].apply(
                lambda x: self.to_uuid(str(int(x))))
        return db['df']
    
    def to_uuid(self, val):
        val += '0'*(32-len(val))
        return f'{val[:8]}-{val[8:12]}-{val[12:16]}-{val[16:20]}-{val[20:]}'
