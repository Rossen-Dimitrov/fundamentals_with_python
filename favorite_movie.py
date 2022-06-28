max_movie_name = ""
max_points = 0
counter = 0
max_inputs = False
while True:
    if counter == 7:
        max_inputs = True
        break
    movie_name = str(input())
    if movie_name == "STOP":
        break
    else:
        cur_points = 0
        counter += 1
        for n in movie_name:
            cur_points += ord(n)
            if n.islower():
                cur_points -= len(movie_name) * 2
            elif n.isupper():
                cur_points -= len(movie_name)
            if cur_points > max_points:
                max_movie_name = movie_name
                max_points = cur_points
if max_inputs:
    print("The limit is reached.")
    print(f"The best movie for you is {max_movie_name} with {max_points} ASCII sum.")
else:
    print(f"The best movie for you is {max_movie_name} with {max_points} ASCII sum.")
