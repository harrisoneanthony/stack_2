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
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookie_order;"
        results = connectToMySQL("cookie_orders").query_db(query)
        all_orders = []
        for order in results:
            all_orders.append( cls(order) )
        return all_orders