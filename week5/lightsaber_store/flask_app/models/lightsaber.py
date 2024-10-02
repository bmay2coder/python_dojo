from flask_app.config.mysqlconnection import connectToMySQL

class Lightsaber:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.level = data['level']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO lightsabers (name, type,level,store_id) VALUES (%(name)s, %(type)s, %(level)s, %(store_id)s);"
        return connectToMySQL('lightsaber_store').query_db(query,data)