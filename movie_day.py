picture_time = int(input())        # 1.	Време за снимки – цяло число в диапазона [0… 1440]
scenes_numbers = int(input())        # 2.	Брой сцени  – цяло число в диапазона [5… 25]
scene_duration = int(input())        # 3.	Времетраене на сцена – цяло число в диапазона [20… 90]
preparation = picture_time * 0.15
total_time = int(scenes_numbers * scene_duration + preparation)
difference = abs(picture_time - total_time)
if total_time <= picture_time:
    print(f"You managed to finish the movie on time! You have {(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {(difference)} minutes.")
