import pymongo
from CRUD.generate_data import bank_account_schema
from CRUD.crud import insert_account, delete_account, get_account

myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@dio-application.knjueno.mongodb.net/?retryWrites=true&w=majority")

#print(myclient)

db_client = myclient["dio-application"]

#print(db_client)

db =  db_client['bank_account']

#print(db)

#create collection 

insert_account(db, bank_account_schema)
get_account(db, 1802)
id_account = input('ID_ACCOUNT TO DELETE ')
delete_account(db, account_number=id_account)
