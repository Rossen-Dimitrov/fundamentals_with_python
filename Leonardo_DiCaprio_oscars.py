user_in = int(input())

if user_in == 88:
    print("Leo finally won the Oscar! Leo is happy")
elif user_in == 86:
    print("Not even for Wolf of Wall Street?!")
elif (not user_in == 88 or not user_in == 86) and user_in < 88:
    print("When will you give Leo an Oscar?")
elif user_in > 88:
    print("Leo got one already!")
