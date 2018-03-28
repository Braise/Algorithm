#Use python3

def GetFibonacciSumNaive(n, m):
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

def GetPartialFibonacciSum(n, m):
    if(n == m):
        return n
    return GetFibonacciSumNaive(n, m)
    
print(GetPartialFibonacciSum(1, 3))
input()