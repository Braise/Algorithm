#Use python3

def LinearSeach(array, toSearch):
    if(len(array) == 0):
        return None

    for i in range(len(array)):
        if(array[i] == toSearch):
            return i
    return None

print(LinearSeach([4, 5, 6, 8, 9, 10], 9))