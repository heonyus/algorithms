a1, a2 = map(int, input().split())
# print(a1, a2) # 2, 5

a = [a1, a2]

for i in range(2, 10):
    if a[i-2]+a[i-1]>=10:
        a.append((a[i-2]+a[i-1])-10)
    else:
        a.append(a[i-2]+a[i-1])

for i in range(len(a)):
    print(a[i], end=" ")