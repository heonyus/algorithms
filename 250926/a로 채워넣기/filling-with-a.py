word = input()

new_word = word.replace(word[1], "a", 1)
new_word_1 = new_word.replace(word[-2], "a", 1)

print(new_word_1)