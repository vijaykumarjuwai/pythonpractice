a = map(int, raw_input().split())
b = map(int, raw_input().split())

b_copy = b[:]

minimum = 0
c = []

'''
for x in range(a[1]):
    c.append(min(b))
    b[:] = [x for x in b if x != min(b)]
'''

for x in range(a[1]):
    c.append(min(b))
    for y in reversed(b):
        if y == min(b):
            b.remove(y)
            break

counter = 0

for x in range(len(c)):
    b_copy[x] = c[x]


e = map(str, b_copy) #This is the trick to convert all elements in list to string

print " ".join(e) #This is the trick to display all string items in list separated by a space