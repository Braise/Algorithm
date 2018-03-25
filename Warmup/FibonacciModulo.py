#Use python3

def EuclidianAlgorithm(a, b):
    if(b == 0):
        return a
    if(a == 0):
        return b
    return EuclidianAlgorithm(b, a%b)

print(EuclidianAlgorithm(14, 15))
input()