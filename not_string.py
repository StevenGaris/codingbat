
def not_string(word):
    if word[:3] == "not":
        return word
    return "not " + word

print(not_string("candy"))
print(not_string("x"))
print(not_string("not bad"))
print(not_string("not"))