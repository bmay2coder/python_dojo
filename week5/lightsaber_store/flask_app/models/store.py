from flask_app.config.mysqlconnection import connectToMySQL
from .lightsaber import Lightsaber

class Store:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.lightsabers = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM stores;"

        results = connectToMySQL('lightsaber_store').query_db(query)
        stores = []

        for d in results:
            stores.append( cls(d) )
        return stores

    @classmethod
    def save(cls, data):
        query= "INSERT INTO stores (name) VALUES (%(name)s);"
        result = connectToMySQL('lightsaber_store').query_db(query,data)
        return result

    @classmethod
    def get_one_with_lightsabers(cls, data ):
        query = "SELECT * FROM stores LEFT JOIN lightsabers on stores.id = lightsabers.store_id WHERE stores.id = %(id)s;"
        results = connectToMySQL('lightsaber_store').query_db(query,data)
        print(results)
        store = cls(results[0])
        for row in results:
            n = {
                'id': row['lightsabers.id'],
                'name': row['lightsabers.name'],
                'type': row['type'],
                'level': row['level'],
                'created_at': row['lightsabers.created_at'],
                'updated_at': row['lightsabers.updated_at']
            }
            store.lightsabers.append( Lightsaber(n) )
        return store