#Use python3

def ChangingMoney(toChange):
    if(toChange == 1 or toChange == 5 or toChange == 10):
        return 1
    i = 0
    while(toChange > 0):
        if(toChange < 5):
            i += toChange
            break
        elif(toChange < 10):
            i += 1
            toChange -= 5
        else:
            temp = toChange % 10
            i += (toChange - temp) // 10
            toChange = temp
    return i

print(ChangingMoney(20123467))