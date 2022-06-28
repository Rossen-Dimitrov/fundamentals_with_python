floors_num = int(input())
rooms_num = int(input())
floor_latter = ""
for floor in range(floors_num, 0, -1):
    for room in range(rooms_num):
        if floor == floors_num:
            floor_latter = "L"
        elif floor % 2 == 0:
            floor_latter = "O"
        else:
            floor_latter = "A"
        print(f"{floor_latter}{(floor * 10 + room)}", end=" ")
    print()



# floors_num = int(input())
# rooms_num = int(input())
#
# for floor in range(floors_num, 0, -1):
#     for room in range(rooms_num):
#         if floor == floors_num:
#             print(f"L{(floor * 10 + room)}", end=" ")
#         elif floor % 2 == 0:
#             print(f"O{(floor * 10 + room)}", end=" ")
#         else:
#             print(f"A{(floor * 10 + room)}", end=" ")
#     print()
#