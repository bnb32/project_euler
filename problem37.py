import math

def isPrime(N):
    if N==1: return False
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0: return False
    return True

def possPrimes(N):
    poss=[N]
    s=str(N)
    for i in range(1,len(s)):
        poss.append(int(s[:i]))
        poss.append(int(s[::-1][:i][::-1]))
    return poss

def main():
    primes=[]
    n=10
    while len(primes)<11:
        if all(isPrime(p) for p in possPrimes(n)):
            primes.append(n)
        n+=1    
    return sum(primes)    


if __name__=="__main__":
    print(main())
