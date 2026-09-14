# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": round(rating, 2)
    }
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
  
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
  
    return user_data

def watch_movie(user_data, title): 

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_length = len(user_data["watched"])

    if watched_length == 0:
        return 0.0
                      
    avg_rating = 0.0

    for movie in user_data["watched"]:
        avg_rating += movie["rating"]

    if avg_rating == 0.0:
        return 0.0  

    return avg_rating/watched_length

def get_most_watched_genre(user_data):
    watched_length = len(user_data["watched"])
    
    if watched_length == 0:
        return None

    popular_movie = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        popular_movie[genre] = popular_movie.get(genre, 0) + 1

    popular_count = 0
    popular_genre = None

    for genre, count in popular_movie.items():
        if count > popular_count:
            popular_count = count
            popular_genre = genre

    return popular_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

