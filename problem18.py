import numpy as np

def quick_sum(mat,N):
    for i in range(N-2,-1,-1):
        for j in range(0,N):
            if j<N-1:
                mat[i,j]=max([mat[i,j]+mat[i+1,j],mat[i,j]+mat[i+1,j+1]])
            else:
                mat[i,j]=mat[i,j]+mat[i+1,j]

    return mat[0,0]        

if __name__=="__main__":
    triangle=np.zeros((15,15),dtype=int)
    f=open('./problem18.txt','r')
    for n,l in enumerate(f.readlines()):
        tmp=l.split()+[0]*(15-len(l.split()))
        triangle[n]=tmp
    print(quick_sum(triangle,15))    
