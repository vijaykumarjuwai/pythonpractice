a = [1, 5, 3, 2, 4, 6, 9, 8, 10, 7]
def bubbleSort(a):
    length = len(a)
    for i in range(length-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a

print bubbleSort(a)

