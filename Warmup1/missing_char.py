
def missing_char(word, num):
    word = list(word)
    del word[num]
    word = "".join(word)
    return word

print(missing_char("Apple",2))
print(missing_char("Human",4))
print(missing_char("Racecar",0))