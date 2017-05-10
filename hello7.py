a = map(int, raw_input().split())
b = map(int, raw_input().split())
c = len(b)
counter = 0
count = 0
for i in range(c):
    if b[i] > a[1]:
        counter += 1
    if counter >= 2:
        break
    if b[i] <= a[1]:
        count += 1


print count