from flask_app.config.mysqlconnection import connectToMySQL

class Burger:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.restaurant_name = 'temp'
    
    @classmethod
    def save( cls , data ):
        query = "INSERT INTO burgers ( name , bun, meat, calories, restaurants_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurants_id)s,NOW(),NOW());"
        return connectToMySQL('burgers').query_db(query,data)

    @classmethod
    def get_all_burgers(cls):
        query = "SELECT burgers.*, restaurants.name FROM restaurants LEFT JOIN burgers ON burgers.restaurants_id = restaurants.id;"
        results = connectToMySQL('burgers').query_db( query )
        print(results)
        all_burgers =[]
        for row_from_db in results:
            burger_data = {
                "id" : row_from_db["id"],
                "name" : row_from_db["name"],
                "bun" : row_from_db["bun"],
                "meat" : row_from_db["meat"],
                "calories" : row_from_db["calories"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"]
            }
            burger_class = Burger( burger_data )
            burger_class.restaurant_name = row_from_db['restaurants.name']
            all_burgers.append( burger_class )
        return all_burgers

    @classmethod
    def get_one_burger(cls,data):
        query = "SELECT burgers.*, restaurants.name FROM restaurants LEFT JOIN burgers ON burgers.restaurants_id = restaurants.id WHERE burgers.id = %(id)s;"
        result = connectToMySQL('burgers').query_db(query,data)
        print(result[0])
        burger_one = cls(result[0])
        burger_one.restaurant_name = result[0]["restaurants.name"]
        return burger_one

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM burgers WHERE id = %(id)s"
        return connectToMySQL('burgers').query_db(query,data)
