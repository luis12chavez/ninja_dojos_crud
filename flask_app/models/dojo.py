from flask_app.config.mysqlconnection import connectToMySQL

# import ninja.py file
from flask_app.models import ninja
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at']
        self.student = None


    # Staticmethod: Because this function does not give functionality to the class Burger
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        return is_valid


    
    @classmethod
    def dojos_available(cls):
        query = "Select * from dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        
        return dojos
    

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT into dojos(name, created_at, updated_at) Values( %(name)s, NOW(), NOW() )"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return result
    

    @classmethod
    def dojo_all_info(cls):
        query = "SELECT * FROM dojos join ninjas on ninjas.dojo_id = dojos.id;" # each row now is of every ninja in every dojos table 
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # print(results)

        dojos = []

        # if statement:  if the query above has no results 
        if results:
            for row in results:
                # convert dojo data from row into class object 
                dojo = cls(row)
                # convert ninja data from row row into class object
                dojo.student = ninja.Ninja(row)
                dojos.append(dojo)
        return dojos
    

    @classmethod
    def students_per_dojo(cls, dojo_id):
        query = f"SELECT * FROM dojos join ninjas on ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = {dojo_id};"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        # print(results)

        for row in results:
            dojo = cls(row)
            dojo.student = ninja.Ninja(row)
            dojos.append(dojo)
        return dojos