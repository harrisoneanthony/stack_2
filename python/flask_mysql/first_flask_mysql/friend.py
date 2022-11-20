# import the function that will return an instance of a connetion

from mysqlconnection import connectToMySQL
#  model the class after the friend table from our database
class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.pdated_at = data['updated_at']
    #  now we use class methods to query our databases``

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting
        results = connectToMySQL('first_flask').query_db(query)
        #  create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )
        return friends

    #  class method to save our friend to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends ( first_name, last_name, occupation, createdat, updated_at ) VALUES ( %(fname)s, %(lname)s, %(occ)s, NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('first_flask').query_db(query,data)