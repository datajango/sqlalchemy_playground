from sqlalchemy import MetaData, create_engine
from sqlalchemy import select, inspect

metadata = MetaData()

db_string = "postgresql+psycopg2://playground:playground@localhost:5432/"
eng = create_engine(db_string)
con = eng.connect()

insp = inspect(eng)
db_list = insp.get_schema_names()
print(db_list)

rows = eng.execute('SELECT datname FROM pg_database;').fetchall()
for rindex, row in enumerate(rows):
    print(f"\t{rindex},{row}")
    #for col in row:
    #    print(col)


#metadata.reflect(bind=eng)
#print(metadata.schema)
#print(schemas)

# tables = metadata.tables.keys()
# for index, table in enumerate(tables):
#     print(index, table)

#     tbl = metadata.tables[table]
#     s = select([tbl]).limit(10)
#     rows = eng.execute(s).fetchall()
#     for rindex, row in enumerate(rows):
#         print(f"\t{rindex},{row}")
#         #for col in row:
#         #    print(col)

con.close()