groups = int(input())
total_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
for _ in range(groups):
    group_members = int(input())
    if group_members <= 5:
        musala += group_members
        total_people += group_members
    elif group_members <= 12:
        monblan += group_members
        total_people += group_members
    elif group_members <= 25:
        kilimandjaro += group_members
        total_people += group_members
    elif group_members <= 40:
        k2 += group_members
        total_people += group_members
    else:
        everest += group_members
        total_people += group_members
print(f"{(musala / total_people) * 100:.2f}%")
print(f"{(monblan / total_people) * 100:.2f}%")
print(f"{(kilimandjaro / total_people) * 100:.2f}%")
print(f"{(k2 / total_people) * 100:.2f}%")
print(f"{(everest / total_people) * 100:.2f}%")
