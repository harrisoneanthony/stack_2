from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users_models
from flask_app.models import purchases_models
from flask import flash


db = 'black_belt_attempt'

class Painting:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.quantity = data['quantity']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.purchased_painting = None
        self.painter = None

    @staticmethod
    def valdiate_painting(painting):
        is_valid = True
        if len(painting['title']) < 1:
            flash("Title must not be left blank.")
            is_valid = False
        if len(painting['description']) < 1:
            flash("Description must not be left blank.")
            is_valid = False
        if int(float(painting['price'])) < 1:
            flash("Please enter a price.")
            is_valid = False
        if int(painting['quantity']) < 1:
            flash("Please enter a quantity")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_paintings(cls):
        query = "SELECT * from painting LEFT JOIN purchase ON painting.id = purchase.painting_id JOIN user on painting.user_id = user.id;"
        results = connectToMySQL(db).query_db(query)
        all_paintings = []
        for row in results:
            one_painting = cls(row)
            one_painting.purchased_painting = purchases_models.Purchase(
                {
                    'user_id': row['user_id'],
                    'painting_id':row['painting_id']
                }
            )
            one_painting.painter = users_models.User(
                {
                'id': row['user.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
                }
            )
            all_paintings.append(one_painting)
        return all_paintings

    @classmethod
    def add_painting(cls, data):
        query = "INSERT INTO painting (title, description, price, quantity, user_id) VALUES (%(title)s, %(description)s, %(price)s, %(quantity)s, %(user_id)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM painting WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query, data)


    @classmethod
    def get_one_painting(cls, data):
        query = "SELECT * FROM painting JOIN user ON user.id = painting.user_id WHERE painting.id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        painting = cls(results[0])
        painting.painter = results[0]['first_name']
        return painting

    @classmethod
    def update(cls,data):
        query = "UPDATE painting SET title = %(title)s, description = %(description)s, price = %(price)s, quantity = %(quantity)s WHERE id = %(id)s;"
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_purchased_paintings(cls, data):
        query = "SELECT * FROM purchase WHERE painting_id = %(id)s"
        return len(connectToMySQL(db).query_db(query,data))

    @classmethod
    def show_all_purchases(cls, data):
        query = "SELECT * from painting LEFT JOIN purchase ON painting.id = purchase.painting_id JOIN user on painting.user_id = user.id WHERE purchase.user_id = %(id)s;"
        results = connectToMySQL(db).query_db(query,data)
        all_purchases = []
        for row in results:
            one_purchase = cls(row)
            one_purchase.purchased_painting = purchases_models.Purchase(
                {
                    'user_id': row['user_id'],
                    'painting_id':row['painting_id']
                }
            )
            one_purchase.painter = users_models.User(
                {
                'id': row['user.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at']
                }
            )
            all_purchases.append(one_purchase)
        return all_purchases
