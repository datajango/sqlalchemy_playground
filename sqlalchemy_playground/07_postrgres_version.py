from sqlalchemy import create_engine

db_string = "postgresql+psycopg2://playground:playground@localhost:5432/pubsdb"
eng = create_engine(db_string)
con = eng.connect()


rs = con.execute("SELECT VERSION()")
print(rs.fetchone())

con.close()