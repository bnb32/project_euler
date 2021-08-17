from collections import defaultdict
import math

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

@memoize
def partitions(n,m):
    if m<1 or n<1: return 0
    elif m==n: return 1+partitions(n,m-1)
    elif m==1: return 1
    else:
        return partitions(n,m-1)+partitions(n-m,m)


@memoize
def farley_series_length(n):
    return sum([euler_totient(i) for i in range(2,n+1)])

def farley_length_in_range(f_min,f_max,d):
    nums=[i for i in range(int(d*f_min),int(d*f_max)+1) if f_min<i/d<f_max and math.gcd(i,d)==1]
    return len(nums)

def coprimes(n):
    nums=[]
    for i in range(1,n//2+1):
        if math.gcd(i,n)==1: 
            nums.append(i)
            nums.append(n-i)
    return nums

@memoize
def __gcd(m,n):
    while n:
        m,n=n,m%n
    return m    

@memoize
def Series(N,n):
    if n==0: return [int(N**0.5),-int(N**0.5),1]
    else:
        s=Series(N,n-1)
        n2=(N-s[1]**2)//s[2]
        n0=int(s[2]/((N**0.5)+s[1]))
        n1=-s[1]-n2*n0
        return [n0,n1,n2]

def simplify_fraction(numer,denom,num):
    n=denom*num+numer
    d=denom
    return [n,d]

@memoize
def Convergent(N,n):
    if n==-1: return [1,0]
    elif n==0: return [Series(N,0)[0],1]
    else: 
        c1=Convergent(N,n-1)
        c2=Convergent(N,n-2)
        return [Series(N,n)[0]*c1[0]+c2[0],Series(N,n)[0]*c1[1]+c2[1]]

def euler_totient_prime(p):
    return p-1

def euler_totient(n):
    count=n
    if n<0: return 0
    if n==0: return 1
    if n==1: return 1
    for p in prime_factors(n):
        count*=(p-1)/p
    return int(count)  

def isNthPower(m,n):
    tmp=m**(1.0/n)
    if round(tmp)**n == m: return True
    return False

def prime_sieve(N):
    primes=[True]*N
    actual_primes=[]
    primes[0]=primes[1]=False
    for n in range(2,N):
        if primes[n]:
            actual_primes.append(n)
            for j in range(n+n,N,n):
                primes[j]=False
    return actual_primes

def isPrime(N):
    if N <= 1: return False
    if N == 2: return True
    if N % 2 == 0: return False
    for n in range(3,int(N**0.5)+1,2):
        if N % n == 0: return False
    return True    

@memoize
def largest_prime_factor(N):
    i=2
    while i*i <= N:
       if N % i == 0:
           N//=i
       else:
           i+=1
    return N

@memoize
def prime_factors(N):
    divisors=defaultdict(int)
    while N % 2 == 0:
        divisors[2]+=1
        N//=2
    for i in range(3,int(N**0.5)+1,2):
        while N % i == 0:
            divisors[i]+=1
            N//=i
    if N > 2: divisors[N]+=1
    return divisors    

@memoize
def factors(N):
    divs=[1]
    for n in range(2,int((N)**0.5)+1):
        if N % n == 0: 
            divs.append(n)
            if N/n!=n:
                divs.append(N//n)
    return divs

def Tri(n):
    return n*(n+1)//2

def Square(n):
    return n*n

def Pent(n):
    return n*(3*n-1)//2

def GeneralizedPent(n):
    if n==0: m=0
    if n % 2 == 0: m=-n//2
    else: m=n//2+1
    return m*(3*m-1)//2

def Hex(n):
    return n*(2*n-1)

def Hept(n):
    return n*(5*n-3)//2

def Oct(n):
    return n*(3*n-2)

def isPent(n):
    val=1/6*(1+(1+24*n)**0.5)
    if val.is_integer(): return True
    return False

def isTri(n):
    val=1/2*(-1+(1+8*n)**0.5)
    if val.is_integer(): return True
    return False

def isHex(n):
    val=1/4*(1+(1+16*n)**0.5)
    if val.is_integer(): return True
    return False

