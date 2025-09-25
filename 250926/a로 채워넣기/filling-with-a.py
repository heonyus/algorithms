word = input()

# new_word = word.replace(word[1], "a", 1)
# new_word_1 = new_word.replace(word[-2], "a", 1)

# print(new_word_1)

word_list = list(word)
word_list[1]= 'a'
word_list[-2]= 'a'

fin_word = "".join(word_list)
print(fin_word)