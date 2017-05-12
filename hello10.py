a = map(int, raw_input().split())
b = map(int, raw_input().split())

index = 1

for x in range(len(b)):
    if(b[x] == a[1]):
        index = x + 1

print index
