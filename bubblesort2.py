num = int(raw_input())
b = map(int, raw_input().split())

def bubbleSort(a):
    length = len(a)
    counter = 0
    for i in range(length-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                counter += 1
                a[j], a[j+1] = a[j+1], a[j]

    return counter

print bubbleSort(b)

