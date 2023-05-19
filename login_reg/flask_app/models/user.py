from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    db = 'login_reg_2'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # READ ALL
    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_users = []
        for one_user in results:
            all_users.append(cls[one_user])
        return all_users

    # CREATE
    @classmethod
    def save_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, email, password)
            VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query, data)

    # READ ONE by id
    @classmethod
    def get_one_user_by_id(cls, data):
        query = """
            SELECT * FROM users
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    

    # READ ONE by email
    @classmethod
    def get_one_user_by_email(cls, data):
        query = """
            SELECT * FROM users
            WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        # If user email is True (len(results) >= 1), user exists.
        # If nothing comes up, user does not, therefore should return False.
        if len(results) < 1:
            return False
        return cls(results[0])

    # VALIDATE
    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data['first_name']) < 2:
            is_valid = False
            flash('First name must be at least 2 characters long.', 'register')
        if len(data['last_name']) < 2:
            is_valid = False
            flash('Last name must be at least 2 characters long.', 'register')
        query = """
            SELECT * FROM users
            WHERE email = %(email)s;
        """
        results = connectToMySQL(User.db).query_db(query, data)
        if len(results) >= 1:
            is_valid = False
            flash('Email already in use.', 'register')
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email format.', 'register')
        if len(data['password']) < 8:
            is_valid = False
            flash('Password must be at least 8 characters long.', 'register')
        if data['password'] != data['confirm']:
            is_valid = False
            flash('Password does not match.', 'register')
        return is_valid
