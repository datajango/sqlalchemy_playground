from sqlalchemy import create_engine

db_string = "postgresql+psycopg2://playground:playground@localhost:5432/pubsdb"
eng = create_engine(db_string)
con = eng.connect()

class Crud():

    def __init__(self, con) -> None:
        self.con = con

    def create(self):
        pass

    def read(self):
        rs = self.con.execute("SELECT * from author order by author_id;")
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

    def update(self):
        pass

    def delete(self):
        pass

my_crud = Crud(con)

my_crud.create()
my_crud.read()
my_crud.update()
my_crud.delete()

con.close()