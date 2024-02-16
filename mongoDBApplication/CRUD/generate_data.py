from faker import Faker
import random


fake = Faker()
bank_account_schema = {
    'account_holder': fake.name(),
    'account_number': random.randint(1000, 10000),
    'balance':random.randint(1, 10000),
    'branch_code' : random.randint(1, 500),
    'bank_name': fake.profile()['company']
}
print(bank_account_schema)