groups = int(input())
total_members = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
for groups in range(groups):
    group_members = int(input())
    total_members += group_members
    if group_members <=5:
        musala += group_members
    elif group_members <= 12:
        monblan += group_members
    elif group_members <= 25:
        kilimandjaro += group_members
    elif group_members <= 40:
        k2 += group_members
    else:
        everest += group_members
print(f"{(musala / total_members) * 100:.2f}%")
print(f"{(monblan / total_members) * 100:.2f}%")
print(f"{(kilimandjaro / total_members) * 100:.2f}%")
print(f"{(k2 / total_members) * 100:.2f}%")
print(f"{(everest / total_members) * 100:.2f}%")

