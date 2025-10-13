target = 25

while True:
    n = int(input())
    if n < target:
        print("Higher")
    elif n > target:
        print("Lower")
    else:
        print("Good")
        break