w = input()

s = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
for i in s:
    if (i[2] in w) or (i[3] in w):
        cnt+=1
        print(i)

print(cnt)