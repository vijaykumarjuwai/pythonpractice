a = raw_input()
arrayLen = int(a)
numbers = raw_input()
myList = numbers.split(' ')

print myList

answer = 1

if (arrayLen == len(myList)):
    for x in myList:
        answer =  answer * long(x) % 1000000007

print long(answer)