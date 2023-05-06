import pymysql.cursors

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '@lphAlpha98',
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = False,
        )
        self.connection = connection

    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print('Running Query:', query)

                cursor.execute(query)
                # INSERT
                if query.lower().find('insert') >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                # SELECT
                elif query.lower().find('select') >= 0:
                    result = cursor.fetchall()
                    return result
                # UPDATE/DELETE
                else:
                    self.connection.commit()
            
            # Return False if query fails
            except Exception as e:
                print('Something went wrong:', e)
                return False
            
            # Close connection
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)