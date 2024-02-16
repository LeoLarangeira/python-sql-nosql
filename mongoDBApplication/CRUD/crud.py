def insert_account(collection,account_data):
    result = collection.insert_one(account_data)
    
    return result.inserted_id

def get_account(collection,account_number ):
    account = collection.find_one({'account_holder' : account_number} ) 
    return account

def delete_account(collection,account_number ):
    account = collection.delete_one({'account_holder' : account_number} ) 
    return account.deleted_count