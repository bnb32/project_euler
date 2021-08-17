from problem3 import prime_factor
from collections import defaultdict

def factors(N):
    facs=defaultdict(int)
    while N!=1:
        tmp=prime_factor(N)
        facs[tmp]+=1
        N//=tmp
    return facs

def smallest_multiple(N):
    facs=defaultdict(int)
    for i in range(2,N):
        tmp=factors(i)
        for t in tmp:
            if facs[t]<tmp[t]:
                facs[t]+=1
    
    num=1
    for f in facs:
        num*=f**facs[f]
    return num

if __name__=="__main__":
    print(smallest_multiple(20))    
