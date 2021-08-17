from euler_project import prime_sieve,isPrime

def count_digits(N):
    s=str(N)
    digits=[int(d) for d in s]
    if max(digits)!=len(digits): return False
    for i in range(1,len(s)+1):
        if s.count(str(i))!=1: return False
    return True    

def main():
    for p in range(10**7-1,2,-2):
        if isPrime(p) and count_digits(p): return p

if __name__=="__main__":
    print(main())
