number_g = int(input())
g_favorite = int(input())
odd = number_g % 2 != 0
negative = number_g < 0
favorite = number_g % g_favorite == 0

if odd and  negative and favorite:
    print('super special awesome')

elif (odd and negative) or (odd and favorite) or (negative and favorite):
    print("super awesome")
elif odd or negative or favorite:
    print('awesome')
else:
    print('boring')
