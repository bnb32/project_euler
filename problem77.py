import euler_project as euler
from collections import defaultdict

def prime_partition(N):
    primes=euler.prime_sieve(N+1)
    sums=set()
    for p in primes:
        sums.add((p,))
    for i in range(1,N//2+1):
        tmp=set()
        for s in sums:
            if sum(s)==N: tmp.add(s)
            else:
                for p in primes:
                    if sum(s)+p<=N:
                        tmp.add(tuple(sorted(s+(p,))))
        sums=tmp
    return len(sums)     
        
def main():
    N=5000
    count=0
    n=2
    while count<=N:
        count=prime_partition(n)
        n+=1
    return n-1,count

if __name__=="__main__": print(main())    
