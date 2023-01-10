from flask_app.config.mysqlconnection import connectToMySQL

db='friendships_schema'

class Friendship:
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.friendship_id = data['friendship_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_friendship(cls,data):
        query = "INSERT INTO friendships (user_id, friendship_id) VALUES ( %(user_id)s, %(friendship_id)s )"
        return connectToMySQL(db).query_db(query,data)

    @staticmethod
    def friendship_checker(data):
        query = "SELECT * FROM friendships WHERE user_id = %(user_id)s AND friendship_id = %(friendship_id)s"
        results = connectToMySQL(db).query_db(query,data)
        print(results)
        if len(results)>0:
            return False
        return True