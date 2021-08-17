from math import sqrt

def isprime(N):
    for i in range(2,int(sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def primes(N):
    tmp=[]
    n=2
    while len(tmp)<N:
       if isprime(n):
           tmp.append(n)
       n+=1    
    return tmp

if __name__=="__main__":
    print(primes(40001)[-1])


