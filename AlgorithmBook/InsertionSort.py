#Use python3

def InsertionSortIncreasing(toSort):
    if(len(toSort) <= 1):
        return toSort

    for i in range(1, len(toSort)):
        key = toSort[i]
        j = i - 1
        while(j >= 0 and toSort[j] > key):
            toSort[j + 1] = toSort[j]
            j -= 1
        toSort[j + 1] = key
    return toSort

def InsertionSortDecreasing(toSort):
    if(len(toSort) <= 1):
        return toSort
    
    for i in range(1, len(toSort)):
        j = i - 1
        key = toSort[i]

        while(j >= 0 and key > toSort[j]):
            toSort[j + 1] = toSort[j]
            j -= 1

        toSort[j + 1] = key
    return toSort

toSort = [5, 7, 1, 2, 6, 10]
print(InsertionSortIncreasing(toSort))
print(InsertionSortDecreasing(toSort))

    