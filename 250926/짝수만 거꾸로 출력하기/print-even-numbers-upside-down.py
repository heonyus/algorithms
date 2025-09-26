n1 = int(input())
n2 = list(map(int, input().split()))

n2.reverse()

# print(n2)
new_lst=[]

for i in range(len(n2)):
    if n2[i] % 2 ==0:
        new_lst.append(n2[i])

for i in range(len(new_lst)):
    print(new_lst[i], end=" ")
