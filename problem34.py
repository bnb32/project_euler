from math import factorial

def sum_check(N,facs):
    val=sum(facs[int(n)] for n in str(N))
    if val==N: return True
    return False

def main():
    val=0
    facs=[factorial(n) for n in range(0,10)]
    for i in range(3,10**7):
        if sum_check(i,facs): val+=i
    return val

if __name__=="__main__": print(main())    
