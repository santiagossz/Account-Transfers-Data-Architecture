import regex as re


class DWH_TABLES():

    def __init__(self):

        super().__init__()
        self.script=[]

    def create_tables(self, file):


        self.tables, self.relations = file.split(
            'Ref')[0], file.split('Ref')[1:]

        self.script=self.format_relations() if self.add_relations else self.format_create_table()
        

    def format_create_table(self):
        self.tables = self.tables.replace('Table', 'CREATE TABLE IF NOT EXISTS').replace(' as U ', ' ').replace('{', '(')\
            .replace('}', ');\n').replace('[pk]', 'PRIMARY KEY,').replace(' int',' bigint')

        self.tables = re.sub('(?<=\)|\w)\n(?!\))', ',',self.tables)

        return self.tables
        

    def format_relations(self):
        self.relations=[self.create_relations(self.relation_elements(r, '\:(?P<e>.+?)\.'), self.relation_elements(r, '\.(?P<e>.+?)\ '),
                            self.relation_elements(r, '(\>|\<|\-)(?P<e>.+?)\.'), self.relation_elements(r, '(?i)\.(?P<e>[^\.]+?)(\n|)$')) 
                            for r in self.relations]
        self.relations=';\n'.join(self.relations)

        return self.relations

    def create_relations(self,fk_table, fk, pk_table, pk):
        return f"""
        ALTER TABLE {fk_table} DROP CONSTRAINT IF EXISTS  {fk_table}_{fk}_fkey; 
        ALTER TABLE {fk_table} ADD CONSTRAINT {fk_table}_{fk}_fkey FOREIGN KEY ({fk})  REFERENCES {pk_table} ({pk})"""

    def relation_elements(self,relations, element):
        return re.search(f'(?i){element}', relations)['e']

       