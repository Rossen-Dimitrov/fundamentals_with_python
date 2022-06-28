def find_kate(mx):
    for r in range(len(mx)):
        for p in range(len(mx[i])):
            if mx[r][p] == 'k':
                return r, p


rows = int(input())
maze = [list(input()) for i in range(rows)]
print(maze)

kate(find_kate(ma))


