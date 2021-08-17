import numpy as np
import math

def walks(Nx,Ny,stored):
    if Nx==0 or Ny==0:
        return 1
    elif Nx==1:
        return 1+Ny
    elif Ny==1:
        return 1+Nx
    elif stored.shape[0]>Nx and stored.shape[1]>Ny and stored[Nx,Ny]!=0:
        return stored[Nx,Ny]
    else:
        return walks(Nx,Ny-1,stored)+walks(Nx-1,Ny,stored)

def binomial(n,k):
    return math.factorial(n)/(math.factorial(n-k)*math.factorial(k))


if __name__=="__main__":
    print(binomial(40,20))
'''
    vals=np.zeros((21,21),dtype=int)
    for i in range(2,21):
        for j in range(2,21):
            vals[i,j]=walks(i,j,vals)
    print(vals[20,20])
'''    
