#Use python3

def ComputGCDSlow(a, b):
    best = 0
    for i in range(1, a+b):
        if(a % i == 0 and b % i == 0):
            best = i
    return best
    
def EuclidianAlgorithm(a, b):
    if(b == 0):
        return a
    if(a == 0):
        return b
    return EuclidianAlgorithm(b, a%b)

def LeastCommonMultiple(a, b):
    return (a*b)//EuclidianAlgorithm(a, b)

print("Euclidian : " + str(EuclidianAlgorithm(226553150, 1023473145)))
print(LeastCommonMultiple(226553150, 1023473145))
#print(ComputGCDSlow(226553150, 1023473145))
print(str(226553150*1023473145))
input()