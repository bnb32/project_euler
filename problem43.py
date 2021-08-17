from itertools import permutations

def divCheck(N):
    primes=[2,3,5,7,11,13,17]
    for i in range(0,len(primes)):
        s=str(N)[i+1:i+4]
        if int(s) % primes[i] != 0:
            return False
    return True 

def main():
    summa=0
    perms=permutations(range(0,10))
    for p in perms:
        s=''
        for d in p:
            s+=str(d)
        if s[0]!=0 and divCheck(int(s)): summa+=int(s)
    return summa

if __name__=="__main__":
    print(main())
