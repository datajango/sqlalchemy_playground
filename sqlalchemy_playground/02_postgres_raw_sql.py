from sqlalchemy import create_engine

db_string = "postgresql+psycopg2://playground:playground@localhost:5432/pubsdb"

eng = create_engine(db_string)
con = eng.connect()

rs = con.execute("SELECT * from author order by author_id;")
#print(rs.fetchone())
columns = rs.keys()
print(columns)
for index, column in enumerate(columns):
    print(index, column, type(column))

rows = rs.fetchall()

for row in rows:
    print(row)
    for index, value in enumerate(row):
        print(f"\t{index}, {value}, {type(value)}")


rs = con.execute("SELECT * from author order by author_id;")
rows = [dict(row) for row in rs.fetchall()]
print(rows)

con.close()