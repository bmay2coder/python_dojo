from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re, string

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.posts = []
    DB = "star_wars_blog"
    caps = string.ascii_uppercase
    numbers = (0,1,2,3,4,5,6,7,8,9)

    @classmethod
    def number_found(cls,name):
        found = False
        for number in cls.numbers:
            if name.find(str(number)) > -1:
                found = True
        return found
    
    @classmethod
    def caps_found(cls,pw):
        found = False
        for letter in cls.caps:
            if pw.find(letter) > -1:
                found = True
        return found

    @classmethod
    def validate_user(cls, user):
        is_valid = True
        if len(user['fname'])<=0:
            flash("First name must not be blank")
            is_valid = False
        if len(user['lname'])<=0:
            flash("Last name must not be blank")
            is_valid = False
        if len(user['password'])<=8:
            flash("Password must be at least 8 chars")
            is_valid = False
        if not cls.number_found(user['password']) or not cls.caps_found(user['password']):
            flash("Password must have at least one capital letter and one number")
            is_valid = False
        if user['password']!=user['confirm']:
            flash("Passwords do not match")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        if not cls.unique_email(user['email']):
            flash("Please choose a different email")
            is_valid = False
        return is_valid
    
    @classmethod
    def validate_login(cls, user):
        is_valid = True
        if len(user['password'])<=8:
            flash("Password must be at least 8 chars")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def unique_email(cls, email):
        query = "SELECT * FROM users where email=%(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, {"email":email})
        if len(results)>0:
            return False
        return True
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(fname)s, last_name=%(lname)s, email=%(email)s, password=%(password)s, updated_at=%(updated_at)s WHERE id = %(id)s"
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, id):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, {"id":id})
    
    @classmethod
    def get_by_id(cls, id):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {"id":id})
        return cls(results[0])
