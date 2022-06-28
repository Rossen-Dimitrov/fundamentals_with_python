first = int(input())
second = int(input())

st_1 = int(first / 1000)
st_2 = int(first / 100) % 10
st_3 = int(first / 10) % 10
st_4 = int(first % 10)

end_1 = int(second / 1000)
end_2 = int(second / 100) % 10
end_3 = int(second / 10) % 10
end_4 = int(second % 10)

for x1 in range(st_1, end_1 + 1):
    for x2 in range(st_2, end_2 + 1):
        for x3 in range(st_3, end_3 + 1):
            for x4 in range(st_4, end_4 + 1):
                if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
                    print(f"{x1}{x2}{x3}{x4}", end=" ")
