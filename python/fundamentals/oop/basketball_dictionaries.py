class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

    @classmethod
    def add_players(cls, data):
        player_objects = []
        for dict in data:
            player_objects.append(cls(dict))
        return player_objects

    def __repr__(self):
        return "Player: {}, {} y/o, pos: {}, team: {}".format(self.name, self.age, self.position, self.team)

kevin = {
    "name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
}

jayson = {
	"name": "Jayson Tatum", 
	"age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age":32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

jaylen = {
    "name": "Jaylen Brown",
    "age": 25,
    "position": "shooting gaurd",
    "team": "Boston Celtics"
}

james = {
    "name": "James Harden",
    "age": 33,
    "position": "point gaurd",
    "team": "Philadelphia 76ers"
}

joel = {
    "name": "Joel Embiid",
    "age": 28,
    "position": "center",
    "team": "Philadelphia 76ers"
}

player_kevin = Player(kevin)
print(player_kevin)
player_jayson = Player(jayson)
print(player_jayson)
player_kyrie = Player(kyrie)
print(player_kyrie)
player_jaylen = Player(jaylen)
print(player_jaylen)
player_james = Player(james)
print(player_james)
player_joel = Player(joel)
print(player_joel)

players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jayson Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, 
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jaylen Brown",
        "age": 25,
        "position": "shooting gaurd",
        "team": "Boston Celtics"
    },
    {
        "name": "James Harden",
        "age": 33,
        "position": "point gaurd",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "Joel Embiid",
        "age": 28,
        "position": "center",
        "team": "Philadelphia 76ers"
    }
]

# for loop over list of dictionaries
    # each time use that dictionary info to 
    # create a new player

new_team = []

for player_dict in players:
    player = Player(player_dict)
    new_team.append(player)

print(new_team)

Player.add_players()