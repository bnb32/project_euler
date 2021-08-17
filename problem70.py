import euler_project as euler

def is_totient_permutation(n):
    m=euler.euler_totient(n)
    m=[int(d) for d in str(m)]
    m.sort()
    tmp=[int(d) for d in str(n)]
    tmp.sort()
    return m==tmp

def is_permutation(m,n):
    m_tmp=[int(d) for d in str(m)]
    m_tmp.sort()
    n_tmp=[int(d) for d in str(n)]
    n_tmp.sort()
    return m_tmp==n_tmp

def main():
    N=10**7
    min_val=N
    n_min=1
    primes=euler.prime_sieve(int(10**4))
    for i in range(len(primes)-1,0,-1):
        for j in range(i,0,-1):
            n=primes[i]; m=primes[j]; num=n*m
            if num<N:
                val=(m-1)*(n-1)
                if is_permutation(num,val):
                    val=num/val
                    if val<min_val: 
                        min_val=val; n_min=num
    return min_val,n_min

if __name__=="__main__": print(main())

