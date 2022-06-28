country = str(input())
tool = str(input())
difficulty = 0
performance = 0

if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif tool == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif tool == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif tool == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif tool == "rope":
        difficulty = 9.500
        performance = 9.400
else:
    if tool == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif tool == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif tool == "rope":
        difficulty = 9.700
        performance = 9.150
total_points = difficulty + performance
lefts = ((20 - total_points) / 20) * 100
print(f"The team of {country} get {total_points:.3f} on {tool}.")
print(f"{lefts:.2f}%")