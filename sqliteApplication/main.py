from sqlalchemy import create_engine, MetaData
from sqlalchemy import Column, Integer, String, ForeignKey
from tables.create_tables import Base, Customer, Account
from sqlalchemy.orm import  Session
from CRUD.crud import get_values, insert_values, delete_values, update_values

 
engine = create_engine("sqlite:///user.db")


with engine.connect() as connection:
     Base.metadata.create_all(engine)
     with Session(engine) as session:
         insert_values(session= session)
         get_values(session)
         input_id = input('Inserte the id ')
         
         update_values(session, input_id)
         
         delete_values(session)