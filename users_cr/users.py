from mysqlconnection import connectToMySQL


class User:
    DB = 'users_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def read_all(cls):
        query = """
            SELECT * FROM users
            ORDER BY last_name;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for u in results:
            users.append(cls(u))
        return users

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email)
            VALUES (%(fname)s, %(lname)s, %(email)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
