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
# Return list of movie user had watched and friend haven't watched
def get_unique_watched(user_data):
    friend_watched = get_friend_watched(user_data)
    my_unique_watched = []

    for movie in user_data["watched"]:
        if movie not in friend_watched:
            my_unique_watched.append(movie)

    return my_unique_watched

# Return list of moive friend had watched and I haven't watched
def get_friends_unique_watched(user_data):
    friend_watched = get_friend_watched(user_data)
    my_watched = user_data["watched"]
    friend_unique_watched = []

    for movie in friend_watched:
        if movie not in my_watched and movie not in friend_unique_watched:
            friend_unique_watched.append(movie)

    return friend_unique_watched

# return movie list that friends have watched
def get_friend_watched(user_data):
    friend_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)

    return friend_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
#  Return recomended movies that in user subscription and user has not watched
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    available_recs = []
    user_subscription = user_data.get("subscriptions", [])
    # get movies in friends_unique_watched is that user have service subscription
    for movie in friends_unique_watched:
        if movie["host"] in user_subscription:
            available_recs.append(movie)

    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# Return list of recomended movie for user friendly watched genre
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    unique_watched = get_available_recs(user_data)

    new_rec_by_genre = []

    for movie in unique_watched:
        if movie["genre"] == most_watched_genre:
            new_rec_by_genre.append(movie)

    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    user_favorite = user_data.get("favorites", [])
    friend_unique_watched = get_friend_watched(user_data)

    print(f"friend_unique_watched_title {len(friend_unique_watched)}")
    friend_unique_watched_title = []

    for movie in friend_unique_watched:
        friend_unique_watched_title.append(movie["title"])

    new_rec_from_favorites = []
    for movie in user_favorite:
        if movie["title"] not in friend_unique_watched_title:
            new_rec_from_favorites.append(movie)

    print(f"new_rec_from_favorites {new_rec_from_favorites}")

    return new_rec_from_favorites