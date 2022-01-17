from collections import Counter

a = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,2]

c = Counter(a)
print(c.items())
print(c.elements())