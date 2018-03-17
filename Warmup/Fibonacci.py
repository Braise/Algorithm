#Use python3

def ComputFibonacciNumberSlow(n):
    if(n == 1 or n == 0):
        return n
    return ComputFibonacciNumber(n - 1) + ComputFibonacciNumber(n - 2)

def ComputFibonacciNumberFast(n):
    if(n <= 1):
        return n
    
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])

    return fibo[n - 1] + fibo[n - 2]

def ComputFibonacciNumberLastDigit(n):
    if(n <= 1):
        return n
    
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append((fibo[i - 1] + fibo[i - 2]) % 10)

    return (fibo[n - 1] + fibo[n - 2]) % 10

fib = ComputFibonacciNumberLastDigit(327305)


print(fib)
input()