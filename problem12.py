from math import sqrt

def triangle_number(N):
    return N*(N+1)//2

def factors(N):
    tmp=[]
    for i in range(1,int(sqrt(N))+1):
        if N % i == 0:
            tmp.append(i)
    if tmp[-1]*tmp[-1]==N:
        return 2*len(tmp)-1
    else:    
        return 2*len(tmp)

def triangle_divide(N):
    divs=0
    n=1
    while divs<N:
       divs=factors(triangle_number(n))
       n+=1
    return triangle_number(n-1)

if __name__=="__main__":
    print(triangle_divide(500))
