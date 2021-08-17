import math

def isPrime(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def filtCheck(N,filts):
    if N==2 or N==5:
        return True
    for s in str(N):
        if int(s) in filts:
            return False
    return True        

def listPrimes(N):
    primes=[]
    filts=[2,4,5,6,8,0]
    for i in range(2,N):
        if filtCheck(i,filts):        
            if isPrime(i):
                primes.append(i)
    return primes            

def rotations(N):
    rots=[N]
    while len(rots)<len(str(N)):
        tmp=str(rots[-1])
        tmp=tmp[-1]+tmp[0:-1]
        rots.append(int(tmp))
    return rots    

def circPrimes(primes):
    circs=[]
    for p in primes:
        if all(c in primes for c in rotations(p)):
            circs.append(p)
    return len(circs)        

if __name__=="__main__":
    primes=listPrimes(10**6)
    print(circPrimes(primes))
