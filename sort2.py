def selectionSort(alist, num):
    for fillslot in range(len(alist)-1, 0, -1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

b = map(int, raw_input().split())
blist = map(int, raw_input().split())
selectionSort(blist, b[1])
answer = map(str, blist)
print " ".join(answer)



