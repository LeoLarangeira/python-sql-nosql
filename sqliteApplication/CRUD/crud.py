from sqlalchemy import select, delete, update
from tables.create_tables import Account, Customer

from uuid import uuid4
from faker import Faker
import random 


fake = Faker()

account_type = ['Cheking account', 'Saving Account', 'Money Market Account', 'CD', 'IRA', 'Brokerage Account']
cpf = str(uuid4())
costumer_id =  random.randint(1000, 10000)
account_type = random.choices(account_type)
Schema_costumer = Customer(
    id = costumer_id,
    name = fake.name(),
    cpf =  cpf[:9],
    address  = fake.address()[:19]
)
Schema_Account = Account(
    id_account = random.randint(1000, 10000),
    account_type = account_type[0],
    bank_branch = str(uuid4()),
    num = random.randint(1000, 10000),
    customer_id = costumer_id
)


def insert_values(session):
    session.add_all([Schema_Account, Schema_costumer])
    session.commit()

def get_values(session):
    # Use a função select() para construir uma consulta SQL
    stmt = select(Customer, Account)
    
    # Execute a consulta e itere sobre os resultados
    for user in session.execute(stmt):
        print(user)
        
    account_stmt = select(Account)
    for account in session.execute(account_stmt):
        print(account)

def delete_values(session):
    stmt = delete(Customer)
    
    session.execute(stmt)
    
    session.commit()
    
    print('DB VALUES WHERE DELETED')
    
    get_values(session)

def update_values(session, customer_id):
    stmt = update(Customer).where(Customer.id == customer_id).values(name = fake.name())
    
    session.execute(stmt)
    session.commit()