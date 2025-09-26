numbers = [int(num) for num in input().split()]
full_numbers=[]

for i in range(numbers[0], numbers[1]+1):
    full_numbers.append(i)

fin_numbers=[]
for i in range(len(full_numbers)):
    if full_numbers[i] % 2 != 0:
        continue
    else:
        fin_numbers.append(full_numbers[i])
# print(fin_numbers)

total = 0
for i in fin_numbers:
    total += i

print(total)
