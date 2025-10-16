a = [list(map(int, input().split()))for row in range(3)]
input()
b = [list(map(int, input().split()))for row in range(3)]

new_marix = []
for i in range(3):
    new_row=[]
    for j in range(3):
        new_row.append(a[i][j] * b[i][j])
    new_marix.append(new_row)

for row in new_marix:
    print(*row)
