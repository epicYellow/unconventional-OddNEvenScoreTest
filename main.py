temp = [25, 16, 28, 54, 72, 5, 0, 99, 61, 37, 82]

def oddNEventest(num):
    return str(num / 2)[len(str(num / 2)) - 1] == "0"

def calcScore(array):
    score = 0
    for number in array:
        if oddNEventest(number) or number == 0:
            print(oddNEventest(number), " even ", number)
            score += 1
        elif oddNEventest(number) == False and number != 5:
            print(oddNEventest(number), " odd ", number)
            score += 3
        elif number == 5:
            print(number) 
            score += 5

    return score

print(calcScore(temp))
