n = int(input())

sum_val = 0

for i in range(1, 101):
# 1 부터 차례대로 100까지 1씩 증가
    sum_val += i
    if sum_val>=n:
        print(i)
        break