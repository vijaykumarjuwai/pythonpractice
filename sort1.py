from operator import itemgetter
data = [[1,27,3], [4,5,6], [7,8,9]]
data.sort(key=itemgetter(1))

print data