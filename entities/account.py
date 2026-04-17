from datetime import datetime
from entities.transaction import Transaction
from entities.user import User

from persistence.db import get_connection
import pymysql

class Account():
    
    def __init__(self, id: int, number: str, creation_date: datetime, user: User, transactions: list):
        self.id = id
        self.number = number
        self.creation_date = creation_date
        self.user = user
        self.transactions = transactions



    @staticmethod
    def get_account_by_id(user_id: int):
        try:
            connection = get_connection()   
            cursor = connection.cursor(pymysql.cursors.DictCursor)    

            sql = "SELECT id, number, creation_date, user_id FROM account WHERE user_id = %s"
            cursor.execute(sql, (user_id,))

            rs = cursor.fetchone()

            if rs:
                user = User.get_by_id(rs["user_id"])
                transactions = Transaction.get_transaction_by_account(rs["id"])

                account = Account(
                    rs["id"],
                    rs["number"],
                    rs["creation_date"],
                    user,
                    transactions
                )

                return account

            return None

        except Exception as ex:
            print(f"Error getting account: {ex}")
            return None

        finally:
            cursor.close()
            connection.close()