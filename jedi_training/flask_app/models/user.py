from flask_app.config.mysqlconnection import connect_to_mysql
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    DB = "users_schema"

    @classmethod
    def validate_user(cls, user):
        is_valid = True
        if len(user['fname'])<=3:
            flash("First name must not be blank")
            is_valid = False
        if len(user['lname'])<=3:
            flash("Last name must not be blank")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if not cls.unique_email(user['email']):
            flash("Please choose a different email")
            is_valid = False
        return is_valid
    
    @classmethod
    def unique_email(cls, email):
        query = "SELECT * FROM users where email=%(email)s;"
        results = connect_to_mysql(cls.DB).query_db(query, {"email":email})
        if len(results)>0:
            return False
        return True

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connect_to_mysql(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
        return connect_to_mysql(cls.DB).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, updated_at=%(updated_at)s WHERE id = %(id)s"
        return connect_to_mysql(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connect_to_mysql(cls.DB).query_db(query, {"id":id})
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connect_to_mysql(cls.DB).query_db(query, {"id":id})
        return cls(results[0])
