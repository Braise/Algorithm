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
    
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n - 1] + fibo[n - 2]

def GetFibonacciModulo(i, m):
    pisanoLenght = GetPisanoPeriod(m)
    k = i % pisanoLenght
    fib = ComputFibonacciNumber(k)
    return fib % m

print(GetFibonacciModulo(2015, 3))
input()