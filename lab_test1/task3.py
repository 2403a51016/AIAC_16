def movie_recommender():
    movies = {
        'Comedy': ['Welcome', 'De Dana Dan', 'The Hangover', 'Superbad'],
        'Horror': ['Conjuring', 'Final Destination', 'The Ring', 'Insidious'],
        'Action': ['Mad Max: Fury Road', 'John Wick', 'Die Hard'],
        'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather'],
        'Sci-Fi': ['Inception', 'Interstellar', 'The Matrix']
    }

    print("Available genres and movies:")
    for genre, movie_list in movies.items():
        print(f"{genre}: {', '.join(movie_list)}")

    user_genre = input("\nEnter your preferred genre: ").strip().title()

    if user_genre in movies:
        print(f"\nMovies available in {user_genre}: {', '.join(movies[user_genre])}")
    else:
        print("Sorry, that genre is not available.")

# Example usage:
movie_recommender()
