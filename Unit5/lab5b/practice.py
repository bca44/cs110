def main():
    movie_ratings = {"Toy Story 2": "100%", "Toy Story": "100%", "Finding Nemo": "99%", "Inside Out": "98%",
                     "Toy Story 3": "98%"}

    movies = ["Toy Story", "Toy Story 2", "Toy Story 3"]

    # print the rating of each movie in movies
    for title in movies:
        print(f"The rating for {title} is {movie_ratings[title]}")
    # extra line
    print()

    # print the rating for each movie in movie_ratings
    for title, rating in movie_ratings.items():
        print(f"The rating for {title} is {rating}")


if __name__ == '__main__':
    main()
