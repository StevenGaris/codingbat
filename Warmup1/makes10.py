
def makes10(a, b):
    return (a == 10 or b == 10) or (a + b == 10)

print(makes10(9,10))
print(makes10(9,9))
print(makes10(9,1))
print(makes10(10,5))
print(makes10(10,10))