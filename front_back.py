
def front_back(word):
    word_mid = word[1:-1]
    return (word[-1] + word_mid + word[0])

print(front_back("apple"))
print(front_back("train"))
print(front_back("monster"))