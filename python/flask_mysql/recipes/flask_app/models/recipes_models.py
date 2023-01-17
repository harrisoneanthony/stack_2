from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'recipes'

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users_id = data['users_id']
        self.posted_by = None

    @staticmethod
    def validated_recipe(recipe):
        is_valid = True # we assume this is true
        if len(recipe['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(recipe['description']) < 2:
            flash("Description must be at least 2 characters.")
            is_valid = False
        if len(recipe['instructions']) < 2:
            flash("Instructions must be at least 2 characters.")
            is_valid = False
        if len(recipe['under_30']) == 0:
            flash("Under 30 must not be left blank.")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls, data):
        query = "SELECT * from recipes JOIN users on users.id = recipes.users_id;"
        results = connectToMySQL(db).query_db(query, data)
        print(results[0])
        return cls(results[0])