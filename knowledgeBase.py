
movies = [

    # --------------------- HISTORY --------------------- 
    {
        "title": "Schindler's List",
        "genre": "History",
        "type": "Feature Film",
        "duration": 195,
        "year": 1993,
        "duration_category": "long"
    },
    {
        "title": "Braveheart",
        "genre": "History",
        "type": "Feature Film",
        "duration": 178,
        "year": 1995,
        "duration_category": "long"
    },
    {
        "title": "1917",
        "genre": "History",
        "type": "Feature Film",
        "duration": 119,
        "year": 2019,
        "duration_category": "medium"
    },
    {
        "title": "13th",
        "genre": "History",
        "type": "Documentary",
        "duration": 100,
        "year": 2016,
        "duration_category": "medium"
    },
    {
        "title": "Lincoln",
        "genre": "History",
        "type": "Feature Film",
        "duration": 150,
        "year": 2012,
        "duration_category": "long"
    },

    # ---------------------  DRAMA --------------------- 
    {
        "title": "The Shawshank Redemption",
        "genre": "Drama",
        "type": "Feature Film",
        "duration": 142,
        "year": 1994,
        "duration_category": "long"
    },
    {
        "title": "Forrest Gump",
        "genre": "Drama",
        "type": "Feature Film",
        "duration": 142,
        "year": 1994,
        "duration_category": "long"
    },
    {
        "title": "Good Will Hunting",
        "genre": "Drama",
        "type": "Feature Film",
        "duration": 126,
        "year": 1997,
        "duration_category": "medium"
    },
    {
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "type": "Feature Film",
        "duration": 117,
        "year": 2006,
        "duration_category": "medium"
    },
    {
        "title": "Black Mirror: Nosedive",
        "genre": "Drama",
        "type": "TV Movie",
        "duration": 63,
        "year": 2016,
        "duration_category": "short"
    },

    # ---------------------  ACTION --------------------- 
    {
        "title": "The Dark Knight",
        "genre": "Action",
        "type": "Feature Film",
        "duration": 152,
        "year": 2008,
        "duration_category": "long"
    },
    {
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "type": "Feature Film",
        "duration": 120,
        "year": 2015,
        "duration_category": "medium"
    },
    {
        "title": "John Wick",
        "genre": "Action",
        "type": "Feature Film",
        "duration": 101,
        "year": 2014,
        "duration_category": "medium"
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "genre": "Action",
        "type": "Animated Film",
        "duration": 117,
        "year": 2018,
        "duration_category": "medium"
    },
    {
        "title": "Mission: Impossible – Fallout",
        "genre": "Action",
        "type": "Feature Film",
        "duration": 147,
        "year": 2018,
        "duration_category": "long"
    },

    # --------------------- COMEDY --------------------- 
    {
        "title": "Home Alone",
        "genre": "Comedy",
        "type": "Feature Film",
        "duration": 103,
        "year": 1990,
        "duration_category": "medium"
    },
    {
        "title": "The Grand Budapest Hotel",
        "genre": "Comedy",
        "type": "Feature Film",
        "duration": 99,
        "year": 2014,
        "duration_category": "medium"
    },
    {
        "title": "Toy Story",
        "genre": "Comedy",
        "type": "Animated Film",
        "duration": 81,
        "year": 1995,
        "duration_category": "short"
    },
    {
        "title": "Superbad",
        "genre": "Comedy",
        "type": "Feature Film",
        "duration": 113,
        "year": 2007,
        "duration_category": "medium"
    },
    {
        "title": "Knives Out",
        "genre": "Comedy",
        "type": "Feature Film",
        "duration": 130,
        "year": 2019,
        "duration_category": "long"
    }
]



# in this part we filter movies by all their diff items, so its easier for you
# in the rules part ( u dont need to write loops all over again)


# get all movies first 
def get_all_movies():
    return movies


# filter by genre
def get_movies_by_genre(genre):
    result = []
    for movie in movies:
        if movie["genre"] == genre:
            result.append(movie)
    return result


# filter by type
def get_movies_by_type(movie_type):
    result = []
    for movie in movies:
        if movie["type"] == movie_type:
            result.append(movie)
    return result


# filter by year
def get_movies_by_year(year):
    result = []
    for movie in movies:
        if movie["year"] == year:
            result.append(movie)
    return result


# filter by year range
def get_movies_by_year_range(min_year, max_year):
    result = []
    for movie in movies:
        if movie["year"] >= min_year and movie["year"] <= max_year:
            result.append(movie)
    return result


# filter by duration (max)
def get_movies_by_max_duration(max_duration):
    result = []
    for movie in movies:
        if movie["duration"] <= max_duration:
            result.append(movie)
    return result


# filter by duration (min)
def get_movies_by_min_duration(min_duration):
    result = []
    for movie in movies:
        if movie["duration"] >= min_duration:
            result.append(movie)
    return result