movie_numbers = int(input())
highest_movie = ""
highest_rating = 0
lowest_movie = ""
lowest_rating = 10
total_rating = 0
for n in range(movie_numbers):
    movie = input()
    rating = float(input())
    total_rating += rating
    if rating > highest_rating:
        highest_movie = movie
        highest_rating = rating
    if rating < lowest_rating:
        lowest_movie = movie
        lowest_rating = rating
print(f"{highest_movie} is with highest rating: {highest_rating}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating}")
print(f"Average rating: {total_rating / movie_numbers:.1f}")
