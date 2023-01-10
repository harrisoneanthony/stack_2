from flask_app.config.mysqlconnection import connectToMySQL

db = 'friendships_schema'

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name) VALUES (%(first_name)s, %(last_name)s)"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        all_users = []
        for user in results:
            all_users.append( cls(user) )
        return all_users

# whatever table your "FROM" is equals the model file
    @classmethod
    def get_all_friendships(cls):
        query = "SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users JOIN friendships ON users.id = friendships.user_id LEFT JOIN users as users2 ON users2.id = friendships.friendship_id;"
        results = connectToMySQL(db).query_db(query)
        all_friendships = []
        for friendship in results:
            all_friendships.append( friendship )
        return all_friendships