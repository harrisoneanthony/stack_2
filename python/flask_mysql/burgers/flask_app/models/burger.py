from flask_app.config.mysqlconnection import connectToMySQL

class Burger:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.bun = db_data['bun']
        self.meat = db_data['meat']
        self.calories = db_data['calories']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated']
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO burgers ( name , bun, meat, calories, restaurants_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query,data)

    