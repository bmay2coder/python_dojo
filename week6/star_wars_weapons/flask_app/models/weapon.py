from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

db = "star_wars_weapons"
class Weapon:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.description = db_data['description']
        self.instructions = db_data['instructions']
        self.date_made = db_data['date_made']
        self.under_3_hours = db_data['under_3_hours']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.creator = None

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM weapons
                JOIN users on weapons.user_id = users.id;
                """
        results = connectToMySQL(db).query_db(query)
        weapons = []
        for row in results:
            this_weapon = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": "",
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            this_weapon.creator = user.User(user_data)
            weapons.append(this_weapon)
        return weapons
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                SELECT * FROM weapons
                JOIN users on weapons.user_id = users.id
                WHERE weapons.id = %(id)s;
                """
        result = connectToMySQL(db).query_db(query,data)
        if not result:
            return False

        result = result[0]
        this_weapon = cls(result)
        user_data = {
                "id": result['users.id'],
                "first_name": result['first_name'],
                "last_name": result['last_name'],
                "email": result['email'],
                "password": "",
                "created_at": result['users.created_at'],
                "updated_at": result['users.updated_at']
        }
        this_weapon.creator = user.User(user_data)
        return this_weapon

    @classmethod
    def save(cls, form_data):
        query = """
                INSERT INTO weapons (name,description,instructions,date_made,under_3_hours,user_id)
                VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_3_hours)s,%(user_id)s);
                """
        return connectToMySQL(db).query_db(query,form_data)

    @classmethod
    def update(cls,form_data):
        query = """
                UPDATE weapons
                SET name = %(name)s,
                description = %(description)s,
                instructions = %(instructions)s ,
                date_made = %(date_made)s,
                under_3_hours = %(under_3_hours)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,form_data)
    
    @classmethod
    def destroy(cls,data):
        query = """
                DELETE FROM weapons
                WHERE id = %(id)s;
                """
        return connectToMySQL(db).query_db(query,data)
    
    @staticmethod
    def validate_weapon(form_data):
        is_valid = True

        if len(form_data['name']) < 3:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(form_data['description']) < 3:
            flash("Description must be at least 3 characters long.")
            is_valid = False
        if len(form_data['instructions']) < 3:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False
        if form_data['date_made'] == '':
            flash("Please input a date.")
            is_valid = False
        if 'under_3_hours' not in form_data:
            flash("Give me time to make the weapon.")
            is_valid = False

        return is_valid