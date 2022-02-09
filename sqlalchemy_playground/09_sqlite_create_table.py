from sqlalchemy import create_engine
from sqlalchemy.sql import text

eng = create_engine('sqlite:///:memory:')

with eng.connect() as con:

    con.execute(text('''CREATE TABLE Cars(Id INTEGER PRIMARY KEY,
        Name TEXT, Price INTEGER)'''))
    rs = con.execute(text('SELECT * FROM Cars'))

    print(rs.keys())