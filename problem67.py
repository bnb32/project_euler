import numpy as np

def quick_sum(mat):
    N=len(mat)
    for i in range(N-2,-1,-1):
        for j in range(0,len(mat[i])):
            mat[i][j]=max([mat[i][j]+mat[i+1][j],mat[i][j]+mat[i+1][j+1]])

    return mat[0][0]        

if __name__=="__main__":
    triangle=[]
    f=open('./p067_triangle.txt','r')
    for l in f.readlines():
        tmp=[int(t) for t in l.split()]
        triangle.append(tmp)
    print(quick_sum(triangle))    
