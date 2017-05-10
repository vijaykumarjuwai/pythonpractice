a = int(raw_input())

b = raw_input()
bList = b.split(' ')
c = raw_input()
cList = c.split(' ')
d = 0
e = []


for i in range(a):
    e.append(int(bList[d]) + int(cList[d]))
    d += 1


f = []

for x in e:
    f.append(str(x))


print " ".join(f)
