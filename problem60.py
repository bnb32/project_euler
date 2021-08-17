from euler_project import prime_sieve, isPrime
from collections import defaultdict

class memoize(object):
	def __init__(self, func):
		self.func = func
		self.cache = {}
	
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val

def goodAdd(prev,n):
    if all(isGoodPair(p,n) for p in prev): return True
    return False

@memoize
def isGoodPair(m,n):
    cat1=int(str(m)+str(n))
    cat2=int(str(n)+str(m))
    if isPrime(cat1) and isPrime(cat2) and m!=n: return True
    return False

def getSets(primes,N,min_sum):
    sets=defaultdict(list)
    tmp=[]
    for i in range(0,len(primes)):
        for j in range(i+1,len(primes)):
            p=primes[i];n=primes[j]
            sp=[p]+sets[p]
            sn=[n]+sets[n]
            if goodAdd(sp,n):
                sets[p]+=[n]
                sp+=[n]
                if len(sp)>=N and sum(sp)<min_sum:
                    tmp.append(sp)
                    min_sum=sum(sp)
                    return sp
            if goodAdd(sn,p):
                sets[n]+=[p]
                sn+=[p]
                if len(sn)>=N and sum(sn)<min_sum:
                    tmp.append(sn)
                    min_sum=sum(sn)
                    return sn
    return tmp            

def main():
    N=5
    pnum=10000
    min_sum=100000
    primes=prime_sieve(pnum)[1:]
    min_set=getSets(primes,N,min_sum)
    return min_set,sum(min_set)

if __name__=="__main__": print(main())    

