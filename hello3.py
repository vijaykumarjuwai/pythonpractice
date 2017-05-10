def findClosestNumber(temp, temp2, x):
    num1 = temp - x
    print num1
    num2 = temp2 - x
    print num2
    if abs(num1) < abs(num2):
        if temp < 67:
            return 67
        elif temp > 127:
            return 127
        else:
            return temp
    elif abs(num1) == abs(num2):
        if temp < temp2:
            if temp < 67:
                return 67
            elif temp > 127:
                return 127
            else:
                return temp
        else:
            if temp2 < 67:
                return 67
            elif temp2 > 127:
                return 127
            else:
                return temp2
    else:
        if temp2 < 67:
            return 67
        elif temp2 > 127:
            return 127
        else:
            return temp2


print findClosestNumber(128, 139, 127)