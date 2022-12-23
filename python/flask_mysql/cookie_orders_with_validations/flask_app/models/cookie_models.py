from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class Cookie_order:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie_name = data['cookie_name']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_order(cookie_order):
        is_valid = True
        if len(cookie_order["name"]) <= 0 or len(cookie_order["cookie_name"]) <= 0 or int(cookie_order["num_of_boxes"]) <= 0:
            flash("All fields required")
            is_valid = False
        if len(cookie_order['name']) < 2:
            flash("Name must be atleast 2 characters.")
            is_valid = False
        if len(cookie_order['cookie_name']) < 2:
            flash("Cookie type must be atleast 2 characters.")
            is_valid = False
        if int(cookie_order['num_of_boxes']) < 1:
            flash("You must add at least 1 box to your order.")
            is_valid = False
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_order;"
        results = connectToMySQL("cookie_orders").query_db(query)
        all_orders = []
        for order in results:
            all_orders.append( cls(order) )
        return all_orders

    @classmethod
    def save(cls, data):
        query = "INSERT INTO cookie_order (name, cookie_name, num_of_boxes) VALUES ( %(name)s, %(cookie_name)s, %(num_of_boxes)s)"
        return connectToMySQL('cookie_orders').query_db(query,data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cookie_order WHERE id = %(id)s"
        results = connectToMySQL('cookie_orders').query_db(query,data)
        return cls(results[0])


    @classmethod
    def update_order(cls, data):
        query = "UPDATE cookie_order SET name = %(name)s, cookie_name = %(cookie_name)s, num_of_boxes = %(num_of_boxes)s WHERE id = %(id)s"
        results = connectToMySQL('cookie_orders').query_db(query,data)
        print(results)
        return results

    @classmethod
    def delete(cls, data):
        query = "DELETE * FROM cookie_order WHERE id = %(id)s"
        return connectToMySQL('cookie_orders').query_db(query,data)

    