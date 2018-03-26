#Use python3
def GetPisanoPeriod(m):
    a = 0
    b = 1
    c = a + b

    for i in range(0, m * m):
        c = (a + b) % m
        a = b
        b = c

        if(a == 0 and b == 1):
            return i + 1

def ComputFibonacciNumber(n):
    if(n <= 1):
        return n

    a = 0
    b = 1
    c = 0
    for _ in range(2, n):
        c = a + b
        a = b
        b = c

    return a + b

def GetFibonacciModulo(i, m):
    pisanoLength = GetPisanoPeriod(m)
    k = i % pisanoLength
    fib = ComputFibonacciNumber(k)
    return fib % m

def GetFibonacciSum(n):
    return GetFibonacciModulo(n + 2, 10) - 1
    #return ComputFibonacciNumber(n + 2) - 1

#print(GetFibonacciSum(100) % 10)
print(GetFibonacciSum(999999))
input()