word = input().split()

if len(word[0]) > len(word[1]):
    print(word[0], len(word[0]))
elif len(word[0]) == len(word[1]):
    print("same")
else:
    print(word[1], len(word[1]))