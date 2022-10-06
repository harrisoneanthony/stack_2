#  dictionaries with lists and dictionaries

movies = {
    'horror': ['Dracula', 'Texas Chain Saw Massacare', 'The Conjuring'],
    'comedy': ['Step Brothers', 'Hot Rod', 'White Chicks', 'Anchorman'],
    'action': ['John Wick', 'Gladiator', 'Dirty Harry', 'Semi Pro', 'Training Day'],
    'sci-fi': ['Back to the Future', "Spiderman: No way home", "Star Wars", 'Puppet master'],
}


# print(movies)
# create a function that adds to the list of the correct genre
def addOne(genre, film):
    if genre not in movies.keys():
        return f'{genre} does not exist'
    movies[genre].append(film)
    return movies


# print(addOne('horror', 'IT'))
# print(addOne('horror', 'Killer clowns from outer space'))
# print(addOne('drama', 'Llama'))


# create a function that adds a new genre and a list of movies onto our dictionary def 
# add_genre_and_list(genre,list)

def add_genre_and_list(genre,movie_list):
    movies[genre] = movie_list
    return movies

print(add_genre_and_list('fantasy', ['harry potter', 'game of thrones', 'house of dragons', 'lord of the rings']))

# creat a function printInfo(some_dict) that given a dictionary whose values are all
# lists, prints the name of each key along with the size of its list, and then prints
# the associated values within each key's list for example:

# {num} Horror
# Dracula
# Texas Chain Saw Massacare


# {num} Comedy
# Step Brothers

def print_info(some_dict):
    for key, val in some_dict.items():
        print(len(val), key)
        for film in val:
            print(film)
print_info(movies)

