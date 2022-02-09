from sqlalchemy import MetaData, create_engine
from sqlalchemy import select

metadata = MetaData()
db_string = 'sqlite:///chinook.db'
eng = create_engine(db_string)
con = eng.connect()

metadata.reflect(bind=eng)

tables = metadata.tables.keys()
for index, table in enumerate(tables):
    print(index, table)

    tbl = metadata.tables[table]
    s = select([tbl]).limit(10)
    rows = eng.execute(s).fetchall()
    for rindex, row in enumerate(rows):
        print(f"\t{rindex},{row}")
        #for col in row:
        #    print(col)

con.close()