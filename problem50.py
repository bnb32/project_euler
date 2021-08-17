from euler_project import prime_sieve,isPrime

def smaller_primes(N,primes):
    i=0
    while primes[i]<N//2: i+=1
    return primes[0:i]

def prime_sum(N,primes,count):
    for i in range(0,len(primes)-(count+1)):
        summa=0
        n=i
        while summa<N and n<len(primes): 
            summa+=primes[n]
            n+=1
        if summa==N: return primes[i:n]
    return False

def main():
    pmin=10**3
    pmax=10**6
    primes=prime_sieve(pmax)
    nums=[]
    prime=0
    count=0
    for p in primes[::-1]:
        if p>pmin:
            #tmp=longer_sum(p,smaller_primes(p,primes),count)
            pnums=smaller_primes(p,primes)
            if sum(pnums[0:count+1])>p:
                return prime,count
            else:    
                tmp=prime_sum(p,pnums,count)
                if tmp!=False:
                    if len(tmp)>count: 
                        nums=tmp
                        count=len(tmp)
                        prime=p
                        print(prime,len(nums))
    return prime,count

if __name__=="__main__":
    #print(prime_sieve(10**6)[-1])
    #primes=[p for p in range(2,10**6) if isPrime(p)]
    print(main())
