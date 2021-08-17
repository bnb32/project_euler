import math
import euler_project as euler
import numpy as np
import decimal

context=decimal.Context(prec=100)

@euler.memoize
def Series(N,n):
    if n==0: return [int(N**0.5),-int(N**0.5),1]
    else:
        s=Series(N,n-1)
        n2=(N-s[1]**2)//s[2]
        n0=int(s[2]/((N**0.5)+s[1]))
        n1=-s[1]-n2*n0
        return [n0,n1,n2]

def getPeriod(N):
    if N**0.5 % 1 == 0: return 0
    
    tmp=[]
    n=0
    while True:
       s=Series(N,n)
       if s in tmp: return n-tmp.index(s)
       tmp.append(s)
       n+=1
    
def main():
    M=2;N=10000;count=0
    for n in range(M,N+1):
        p=getPeriod(n)
        if p % 2 == 1: 
            print(n)
            count+=1
    return count    

if __name__=="__main__": 
    print("count: %s"%main())
    
