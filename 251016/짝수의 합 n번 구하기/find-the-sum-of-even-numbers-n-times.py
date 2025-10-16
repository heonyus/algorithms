n = int(input())

for _ in range(n):
    a, b = map(int, input().strip().split())
    s = []
    for i in range(a, b+1):
        if i % 2 == 0:
            s.append(i)
    print(sum(s))
