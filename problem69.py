import euler_project as euler

def isCoprime(m,n):
    return euler.__gcd(m,n)==1

def euler_totient(n):
    count=n
    for p in euler.prime_factors(n):
        count*=(p-1)/p#k**(v-1)*(k-1)
    return count    

def main():
    N=10**6
    max_val=0
    max_n=0
    for i in range(2,N+1):
        val=i/euler_totient(i)
        if val>max_val:
            max_val=val; max_n=i
    return max_n,max_val
       
if __name__=="__main__": 
    print(main())       
