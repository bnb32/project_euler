def iter_rule(N):
    if N % 2 == 0:
        return N//2
    else:
        return 3*N+1

def iterations(N):
    num=0
    while N!=1:
        N=iter_rule(N)
        num+=1
    return num

def iterate_all(N):
    steps=0
    val=0
    for i in range(1,N):
        tmp=iterations(i)
        if tmp>steps: 
            steps=tmp
            val=i
    return val

if __name__=="__main__":
    print(iterate_all(10**6))
