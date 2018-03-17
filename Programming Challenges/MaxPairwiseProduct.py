#Uses python3
from random import randint
import array

# n = int(input())
# integers = [int(x) for x in input().split()]

def NaiveMaxPairWise(n, integers):

    product = 0

    for i in range(n):
        for j in range(i + 1, n):
            product = max(product, integers[i] * integers[j])

    return product

def FastMaxPairWise(n, integers):
    index = 0

    for i in range(1, n):
        if(integers[i] > integers[index]):
            index = i
    integers[n-1], integers[index] = integers[index], integers[n-1]

    index = 0
    for i in range(1, n - 1):
        if(integers[i] > integers[index]):
            index = i
    return integers[index] * integers[n - 1]

def StressTest(n, m):
    while True:
        counter = randint(2, n)
        numbers = []
        for i in range(counter):
            numbers.append(randint(0, m))

        naive = NaiveMaxPairWise(counter, numbers)
        fast = FastMaxPairWise(counter, numbers)

        if(naive == fast):
            print("OK")
        else:
            print("KO")
            print(str(numbers))
            print("(" + str(naive) + ", " + str(fast) + ")")
            break;
    input();

StressTest(5, 9)
