import math
import re

def candidates(N):
    s=str(N)
    cands=[]
    for d in s:
        if s.count(d)>1:
            idx=[i for i,x in enumerate(s) if x==d]
            
            tmp=s
            for i in idx:
                tmp=insert_string(tmp,i)
                if tmp not in cands:
                    cands.append(tmp)
            tmp=s
            for i in idx[::-1]:
                tmp=insert_string(tmp,i)
                if tmp not in cands:
                    cands.append(tmp)
           
    return cands

def check_lens(strs):
    for t in strs:
        if len(t.lstrip('0'))!=len(t):
            return False
    return True        

def check_cands(cands,N):
    for n in cands:
        tmp=[]
        for i in range(0,10):
            p=re.sub('-',str(i),n)
            if isPrime(int(p)):
                tmp.append(p)
        if len(tmp)>=N and check_lens(tmp):
            return tmp
    return []       
            
def insert_string(s,i):
    return s[:i]+'-'+s[i+1:]

def check_digits(N):
    if len(str(N))!=len(set(str(N))):
        return True
    return False    

def isPrime(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def main():
    N=8
    for p in range(10**4,10**6):
        if check_digits(p) and isPrime(p):
            pout=check_cands(candidates(p),N)
            if len(pout)>0:
                return pout
    return []

if __name__=="__main__": 
    print(main())    
