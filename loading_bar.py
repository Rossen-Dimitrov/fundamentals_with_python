def loading_bar(percent):
    percent_div = percent // 10
    if percent_div == 10:
        print("100% Complete!\n[%%%%%%%%%%]")
    else:
        print(f'{percent}% [{"%" * percent_div}{"." * (10 - percent_div)}]\nStill loading...')


loading_bar(int(input()))
