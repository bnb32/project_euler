from euler_project import isPrime

def goldbach_check(n,p):
    return ((n-p)/2)**0.5 % 1 == 0

def full_gb_check(n):
    p=n-2
    while p>2:
        if isPrime(p):
            if goldbach_check(n,p):
                return True
        p-=2
    return False

def main():
    n=33
    while True:
        if not isPrime(n):
            if not full_gb_check(n):
                return n
        n+=2

if __name__=="__main__": print(main())

