a = int(raw_input())

while a > 0:
    e = raw_input()
    b = map(int, raw_input().split())

    c = min(b)

    counter = 0

    for x in b:
        if x == c:
            counter += 1

    if counter % 2 == 0:
        print 'Unlucky'
    else:
        print 'Lucky'

    a = a - 1

'''
This is an alternate solution

t=input() #test cases 
while t>0:
    x=input() #fake input 
    y=list()
    y=map(int,raw_input().split(" ")) #number storing 
    t2=y.count(min(y))
    if(t2%2!=0):
        print "Lucky"
    else :
        print "Unlucky"
    t=t-1
'''
