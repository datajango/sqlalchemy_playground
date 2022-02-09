from sqlalchemy import (create_engine, Table, Column, Integer,
    String, MetaData)

meta = MetaData()
cars = Table('person', meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('middle_name', String),
)

# print("The Name column:")
# print cars.columns.Name
# print cars.c.Name

# print "Columns: "
# for col in cars.c:
#     print col

# print "Primary keys:"
# for pk in cars.primary_key:
#     print pk

# print "The Id column:"
# print cars.c.Id.name
# print cars.c.Id.type
# print cars.c.Id.nullable
# print cars.c.Id.primary_key