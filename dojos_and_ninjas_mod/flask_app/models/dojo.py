from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo:
    DB = 'dojos_and_ninjas_schema'

    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas =[]

    @classmethod
    def display_all(cls):
        query = """
            SELECT * FROM dojos;
        """
        all_dojos = connectToMySQL(cls.DB).query_db(query)
        results = []
        for one_dojo in all_dojos:
            results.append(cls(one_dojo))
        return results

    @classmethod
    def display_one(cls, data):
        query = """
            SELECT * FROM dojos
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s;
        """
        one_dojo = connectToMySQL(cls.DB).query_db(query, data)
        results = cls(one_dojo[0])
        for db_row in one_dojo: 
            one_ninja = {
                'id': db_row['ninjas.id'],
                'first_name': db_row['first_name'],
                'last_name': db_row['last_name'],
                'age': db_row['age'],
                'created_at': db_row['ninjas.created_at'],
                'updated_at': db_row['ninjas.updated_at'],
            }
            results.ninjas.append(Ninja(one_ninja))
        return results

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(dojo_name)s);
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
