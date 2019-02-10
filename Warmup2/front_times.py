
# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

def front_times(word, n):
    return word[:3] * n

print(front_times("Apple", 4))
print(front_times("Saxophone", 6))
print(front_times("at", 3))