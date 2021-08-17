import math

def isPrime(N):
    if N<2:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def quadratic(n,a,b):
    return int(n*n+a*n+b)

def countPrimes(a,b):
    n=0
    count=0
    while isPrime(quadratic(n,a,b)):
        count+=1
        n+=1
    return count

def quad_product(N):
    prod=0
    count=0
    for a in range(1-N,N):
        for b in range(-N,N+1):
            tmp=countPrimes(a,b)
            if tmp>count:
                prod=a*b
                count=tmp
    return prod,count                

if __name__=="__main__":
    print(quad_product(1000))
