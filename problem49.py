from euler_project import isPrime

def list_primes(N):
    primes=[p for p in range(10**(N-1),10**N) if isPrime(p)]
    return primes

def same_digits(p,n):
    for d in str(n):
        if str(n).count(d)!=str(p).count(d):
            return False
    return True        

def group_primes(primes):
    groups=[]
    for p in primes:
        tmp=[p]
        for n in primes:
            if p!=n and same_digits(p,n):
                tmp.append(n)
        if len(tmp)>=3: 
            groups.append(tmp)
    return groups

def test_groups(groups):
    for g in groups:
        tmp=g.copy()
        tmp.sort()
        tmp=[tmp[i+1]-tmp[i] for i in range(0,len(tmp)-1)]
        for i in range(0,len(tmp)-1):
            if tmp[i]==tmp[i+1]:
                return str(g[i])+str(g[i+1])+str(g[i+2])
    return []            

def main():
    primes=list_primes(4)
    groups=group_primes(primes)
    return test_groups(groups)

if __name__=="__main__": print(main())    
