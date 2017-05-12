import sys
num = int(raw_input())
length = int(raw_input())
sortedArr = sorted(map(int, raw_input().strip().split(" ")))

for x in range(length):
    if (sortedArr[x] == num):
        print x
        break