from problem7 import isprime

def sum_primes(N):
    tmp=0
    for i in range(2,N):
        if isprime(i):
            tmp+=i
    return tmp

if __name__=="__main__":
    print(sum_primes(2*10**6))
