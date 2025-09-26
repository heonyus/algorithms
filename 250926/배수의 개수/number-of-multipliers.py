arr =[]
for i in range(10):
    arr.append(int(input()))

# print(arr)
new_arr_3=[]
new_arr_5=[]

for i in range(10):
    if arr[i-1] % 3 == 0:
        new_arr_3.append(arr[i-1])
    if arr[i-1] % 5 == 0:
        new_arr_5.append(arr[i-1])

print(len(new_arr_3), end =" ")
print(len(new_arr_5))
