import math
import euler_project as euler
from collections import defaultdict
import numpy as np

A=np.array([[1,-2,2],[2,-1,2],[2,-2,3]])
B=np.array([[1,2,2],[2,1,2],[2,2,3]])
C=np.array([[-1,2,2],[-2,1,2],[-2,2,3]])

sums=defaultdict(int)

def tree_of_triples(t,N):
    summa=sum(t)
    if summa <= N:
        for i in range(summa,N+1,summa):
            sums[i]+=1
        tree_of_triples(A@t,N)
        tree_of_triples(B@t,N)
        tree_of_triples(C@t,N)

def all_triples(N):
    triples=set()
    for m in range(3,int((N)**0.5)+1,2):
        for n in range(m-2,0,-2):
            if math.gcd(m,n)==1:
                a=m*n
                b=(m**2-n**2)//2
                c=(m**2+n**2)//2
                if a+b+c<=N:
                    triples.add((a,b,c))
    return triples        

def count_sums(N):
    sums=[0]*(N+1)
    triples=all_triples(N)
    for t in triples:
        summa=sum(t)
        for i in range(summa,len(sums),summa):
            sums[i]+=1
    return sums

def main():
    N=15*10**5
    tree_of_triples([3,4,5],N)
    return len([s for s in sums.values() if s==1])

if __name__=="__main__": 
    #print(full_triple_tree(24))
    #print(tree_of_triples([3,4,5]))
    print(main())    
