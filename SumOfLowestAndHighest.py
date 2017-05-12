a = map(int, raw_input().strip().split(" "))
b = []
b[:] = [x for x in a if x != max(a)]
c = []
c[:] = [x for x in a if x != min(a)]

sum1 = long(sum(b))
sum2 = long(sum(c))
sum3 = long(sum(a))

if sum1 - sum2 != 0:
    print("{0} {1}".format(str(sum1), str(sum2)))
else:
    aCopy = a[:]
    aCopy.pop()
    sum3 = long(sum(aCopy))
    print("{0} {1}".format(str(sum3), str(sum3)))

'''
d = []
d.append(sum(b))
d.append(sum(c))
d = map(long, d)
d = map(str, d)
e = " ".join(d)
print e
'''

'''
#THis is an alternate solution
a = sorted(map(int,raw_input().split()))
print sum(a[:4]),sum(a[1:])
'''