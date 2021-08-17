import numpy as np

def corner_sum(N):
    tmp=N*N
    for i in range(1,4):
        tmp+=(N*N-(N-1)*i)
    return tmp

def diag_sum(N):
    tmp=1
    for i in range(3,N+1,2):
        tmp+=corner_sum(i)
    return tmp    

if __name__=="__main__":
    print(diag_sum(1001))
