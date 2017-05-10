import math

testCases = int(raw_input())
answers = []

while(testCases > 0):
    lengthOfString = raw_input()
    word = raw_input()
    splitWord = []
    ascVals = []
    newVal = []

    splitWord = list(word)

    for x in word:
        ascVals.append(ord(x))

    def is_prime(n):
        if n == 2:
            return False
        if n % 2 == 0 or n <= 1:
            return True

        sqr = int(math.sqrt(n)) + 1

        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return True
        return False


    def findClosestNumber(temp, temp2, x):
        num1 = temp - x
        num2 = temp2 - x
        if abs(num1) < abs(num2):
            if temp <= 67:
                return 67
            elif temp >= 123:
                return temp2
            else:
                return temp
        elif abs(num1) == abs(num2):
            if temp < temp2:
                if temp <= 67:
                    return 67
                elif temp >= 123:
                    return temp2
                else:
                    return temp
            else:
                if temp2 < 67:
                    return 67
                elif temp2 >= 123:
                    return temp
                else:
                    return temp2
        else:
            if temp2 <= 67:
                return 67
            elif temp2 >= 123:
                return temp
            else:
                return temp2

    def changeVal(x):
            temp = x
            temp2 = x
            while is_prime(temp):
                temp += 1
            while is_prime(temp2):
                temp2 -= 1
            return findClosestNumber(temp, temp2, x)

    for x in ascVals:
        if is_prime(x):
            x = changeVal(x)
        newVal.append(x)

    myStr = ''

    for x in newVal:
        if x >= 67:
            myStr += (chr(x))
        else:
            myStr += chr(67)

    answers.append(myStr)
    testCases -= 1

for x in answers:
    print x
