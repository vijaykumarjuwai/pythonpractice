a = int(raw_input())

answers = []

while a > 0:
    b = raw_input().lower()
    c = list(b)
    counter = 0
    for x in c:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            counter += 1
    answers.append(counter)
    a = a - 1

for x in answers:
    print x


'''
# This is an alternate solution
# Take the number of strings as input
num = int(raw_input())
 
for delta in range(num):
    line_of_trees = raw_input()
    line_of_trees = line_of_trees.lower()
    c = 0
    for i in "aeiou":
        c = c + line_of_trees.count(i)
        
    print c
'''