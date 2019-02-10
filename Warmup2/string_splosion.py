
# Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(word):
    new_word = ""
    for i in range(len(word)):
        new_word = new_word + word[:i+1]
    return new_word

print(string_splosion("Code"))
print(string_splosion("Saxophone"))
print(string_splosion("Apple"))
