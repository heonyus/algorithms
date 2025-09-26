n = int(input())

new_list=[]
for i in range(1, n):
    if (i%2==0)or(i%3==0)or(i%5==0):
        continue
    else:
        new_list.append(i)

print(len(new_list))