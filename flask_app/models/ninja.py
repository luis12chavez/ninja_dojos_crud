from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo

class Ninja: 
    def __init__ (self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.age = data['age']
        Dojo = None

    @classmethod
    def add_ninja(cls, data):
        query = "Insert INTO ninjas (id, dojo_id, first_name, last_name, created_at, updated_at, age) Values( %(id)s, %(dojo_id)s, %(first_name)s, %(last_name)s , NOW(), NOW(), %(age)s )"
        result = connectToMySQL('dojos_and_ninja_schema').query_db(query, data)
        return result 

    @classmethod
    def show_ninjas(cls):
        query = "Select * From ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
