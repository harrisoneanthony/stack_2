from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users_models
from flask import flash


db = 'black_belt_attempt'

class Purchase:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.painting_id = data['painting_id']


    @classmethod
    def purchase(cls, data):
        query = "INSERT INTO purchase (user_id, painting_id) VALUES (%(user_id)s, %(painting_id)s);"
        print(query,data)
        return connectToMySQL(db).query_db(query, data)