
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

print(parrot_trouble(True, 6))
print(parrot_trouble(False, 6))
print(parrot_trouble(True, 8))
print(parrot_trouble(False, 12))
print(parrot_trouble(True, 19))
print(parrot_trouble(True, 22))
print(parrot_trouble(False, 22))
