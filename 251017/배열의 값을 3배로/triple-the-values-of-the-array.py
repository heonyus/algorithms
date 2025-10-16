matrix = [
    list(map(int, input().split())) for row in range(3)
    ]

new_matrix = []
for row in matrix:
    new_row = []
    for element in row:
        new_element = element * 3
        new_row.append(new_element)
    new_matrix.append(new_row)

for row in new_matrix:
    print(*row)