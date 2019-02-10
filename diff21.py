
def diff21(num):
    if num > 21:
        return (num - 21) * 2
    else:
        return 21 - num

print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(30))