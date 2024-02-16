from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cpf = Column(String(9))
    address = Column(String(20))
    
    accounts = relationship('Account', backref='customer')
    
    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, cpf={self.cpf}, address={self.address})"


class Account(Base):
    __tablename__ = 'accounts'
    
    id_account = Column(Integer, primary_key=True, autoincrement=True)
    account_type = Column(String, nullable=False)
    bank_branch = Column(String)
    num = Column(Integer)
    
    customer_id = Column(Integer, ForeignKey('customers.id'))



