n, m = map(int, input().split())
a = [list(map(int, input().split())) for row in range(n)]
b = [list(map(int, input().split())) for row in range(n)]

new_matrix = []
for i in range(n):
    new_row = []
    for j in range(m):
        if a[i][j] == b[i][j]:
            new_row.append(0)
        else:
            new_row.append(1)
    new_matrix.append(new_row)


for row in new_matrix:
    print(*row)
