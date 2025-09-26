n = int(input())

b = [0]

for i in range(1, 10):
# 1 부터 차례대로 100까지 1씩 증가
    b.append(i + b[i-1])
    if b[-1]>n:
        break

print(b[-2])
