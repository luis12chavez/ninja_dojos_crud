from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']


    @classmethod
    def show_all(cls):
        query = "Select * From dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        print(results)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT into dojos(name, created_at, updated_at) Values( %(name)s, NOW(), NOW() )"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result