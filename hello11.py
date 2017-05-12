a = int(raw_input())
answer = []
while a > 0:
    b = raw_input().lower()
    c = list(b)
    c = [x for x in c if x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u']
    answer.append("".join(c))
    a = a - 1

print answer



