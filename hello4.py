aLen = int(raw_input())
arr = []
while aLen > 0:
    aLen -= 1
    inp = raw_input()
    arr.append(inp)

b = len(arr)

while b > 0:
    print arr[b-1]
    b -= 1