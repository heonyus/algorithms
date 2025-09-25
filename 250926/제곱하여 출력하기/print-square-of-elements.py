n = int(input())
new_lst = list(map(int, input().split()))

new_lst = [i**2 for i in new_lst]

for i in range(len(new_lst)):
    print(new_lst[i], end = " ")