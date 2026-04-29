from enum.value_permision import ValuePermission
from persistence.db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql

class Permission:
    def __init__(self, id: int, value: ValuePermission):
        self.id = id
        self.value = value  

            
    def get_by_id(id_user):
            try:
                connection = get_connection()
                cursor = connection.cursor(pymysql.cursors.DictCursor)
                
                sql = "SELECT id, value from permission WHERE id_user = %s"
                cursor.execute(sql, (id_user,))

                rs = cursor.fetchall()
                
                cursor.close()
                connection.close()

                permission = []

                for r in rs:
                     permission.append(Permission(
                          r["id"],
                          ValuePermission(r['value'])))
        
                return permission
            except Exception as ex:
                print(f"Error login user:{ex}")
                return []