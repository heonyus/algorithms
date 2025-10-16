a = [
    list(map(int, input().split())) for row in range(4)
]


for i in a:
    print(sum(i), end ="\n")

