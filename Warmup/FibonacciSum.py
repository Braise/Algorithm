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

def GetPartialFibonacciSumNaive(n, m):
    if(m <= 2):
        return m

    sumParam = 0

    if(n == 1):
        sumParam = 1

    fibo = [0, 1]
    for i in range(2, m):
        fibo.append(fibo[i - 1] + fibo[i - 2])
        if(i >= n):
            sumParam += fibo[i - 1] + fibo[i - 2]

    return sumParam + (fibo[m - 1] + fibo[m - 2])

def GetFibonacciModulo(i, m):
    pisanoLength = GetPisanoPeriod(m)
    k = i % pisanoLength
    fib = ComputFibonacciNumber(k)
    return fib % m
  
def GetFibonacciSum(n):
    return GetFibonacciModulo(n + 2, 10) - 1

def GetPartialFibonacciSum(n, m):
    if(n == m):
        return GetFibonacciModulo(n, 10)
    
    if(n == 0):
        n += 1

    period = GetPisanoPeriod(10)
    partialSum = GetPartialFibonacciSumNaive(n%period, m%period)

    return partialSum % 10
    
print(GetPartialFibonacciSum(10, 10))
input()