import pymysql
from datetime import datetime
from enums.transaction_type import TransactionType
from persistence.db import get_connection

class Transaction:
    def __init__(self, id:int ,date:datetime  , description: str, amount: float ,type:int):
        self.id = id
        self.amount = amount
        self.type = type
        self.description = description
        self.date = date
    
    def get_transaction_by_account(id_account: int):
        try:
            connection = get_connection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = "SELECT id, amount , description,date, type FROM transaction WHERE id_account = %s "
            cursor.execute(sql, (id_account,)) 
            
            
            transactions = cursor.fetchall()
            
            cursor.close()
            connection.close()
            return transactions
            
        except Exception as ex:
            print(f"Error con las transacciones: {ex}")
            return [] 


