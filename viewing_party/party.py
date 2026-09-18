# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or rating is None or rating < 0:
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

# Add movie to watched and remove movie from watchlist
def watch_movie(user_data, title): 
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# Return average rating of user watched movies
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]

    if not watched_movies:
        return 0.0

    total_rating = 0.0

    for movie in watched_movies:
        total_rating += movie["rating"]

    return total_rating / len(watched_movies)

# Return most watched genre of user watched movies
def get_most_watched_genre(user_data):
    user_watched = user_data["watched"]
    
    if not user_watched:
        return None

    genre_counts = {}

    # Get genre form user data "watched" and add to map "genre count" with count
    for movie in user_watched:
        genre = movie["genre"]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    # Compare counts of each genre to get the highest count 
    # and return the genre with highest count
    highest_count = 0
    most_watched_genre = None

    for genre, count in genre_counts.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Return all movies watched by friends
def get_friend_watched(user_data):
    friend_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    return friend_watched

# Return list of movies 
# 1. user had watched and 
# 2. friend haven't watched
def get_unique_watched(user_data):
    friend_watched = get_friend_watched(user_data)
    user_watched = user_data["watched"] 
    user_unique_watched = []
    
    for movie in user_watched:
        if movie not in friend_watched:
            user_unique_watched.append(movie)

    return user_unique_watched

# Return list of movies:
# 1. user has not watched
# friends watched

def get_friends_unique_watched(user_data):
    friend_watched = get_friend_watched(user_data)
    user_watched = user_data["watched"]
    friend_unique_watched = []

    for movie in friend_watched:
        if movie not in user_watched and movie not in friend_unique_watched:
            friend_unique_watched.append(movie)

    return friend_unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# Return movies friends watched that:
# 1. user has not watched
# 2. user subscribed to the movie's host subscription service
# 3. movie in friends unique watched
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    user_subscription = user_data.get("subscriptions", [])
    available_recs = []
    
    # get movies in friends_unique_watched is that user have service subscription
    for movie in friends_unique_watched:
        if movie["host"] in user_subscription:
            available_recs.append(movie)

    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# Return list of recomended movies for 
# 1. user most watched genre 
# 2. user havent watched and 
# 3. friend has watched
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    available_recs = get_available_recs(user_data)

    new_rec_by_genre = []

    for movie in available_recs:
        if movie["genre"] == most_watched_genre:
            new_rec_by_genre.append(movie)

    return new_rec_by_genre

# return recomended movies 
# 1. from user favorites list 
# 2. friends haven't watched
def get_rec_from_favorites(user_data):
    user_favorite = user_data.get("favorites", [])
    friend_watched = get_friend_watched(user_data)

    # get list of recomended movie from user favorites that friends haven't watched
    new_rec_from_favorites = []
    for movie in user_favorite:
        if movie not in friend_watched:
            new_rec_from_favorites.append(movie)

    return new_rec_from_favorites