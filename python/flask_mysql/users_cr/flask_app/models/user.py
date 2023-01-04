from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True

        if len(user["first_name"]) <= 0 or len(user["last_name"]) <= 0 or len(user["email"]) <= 0:
            flash("All fields required")
            is_valid = False
        if len(user["first_name"]) == 0:
            flash("First name cannot be left blank", "First name")
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters", "First name")
            is_valid = False
        if len(user["last_name"]) == 0:
            flash("Last name cannot be left blank", "Last name")
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters", "Last name")
        if len(user["email"]) <= 0:
            flash("Email cannot be left blank", "Email")
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address", "Email")
            is_valid = False

        #     # # SENSEI way using a for loop (Good for if there are many fields)
        # # # Loop over the dictionary with the user data
        # for field in user:
        # #     # Test if any of the entered values are empty strings
        #     if len(user[field]) <= 0:
        #         is_valid = False
        #         message = f"{field} is required.".capitalize()
        # #         # Take the _ out of the field names
        #         make_pretty = message.maketrans("_", " ")
        #         flash(message.translate(make_pretty))
                
        if len(user["email"]) > 0 and not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email format")
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name, last_name, email, created_at, updated_at ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() )"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('users_schema').query_db(query,data)
