from euler_project import Convergent

def getSeries(N,n):
    nums=[]
    for i in range(0,n):
        nums.append(Series(N,i)[0])
    return nums    

def quadDioSoln(D):
    if D**0.5 % 1 == 0: return [0]
    n=1
    [x,y]=Convergent(D,n)
    while (x*x-D*y*y)!=1:
        n+=1
        [x,y]=Convergent(D,n)
    return [x,y]    

#def quadDioSoln(D):
#    if D**0.5 % 1 == 0: return [0]
#    y=1
#    x=(1+D)**0.5
#    while x % 1 != 0: 
#        y+=1
#        x=(1+D*y*y)**0.5
#    
#    return [int(x),int(y)]

def main():
    xs=[]
    N=1000
    for d in range(2,N+1):
        x=quadDioSoln(d)[0]
        xs.append(x)
        print("D,x: %s, %s"%(d,x))
    maxx=max(xs)
    return 2+xs.index(maxx)

if __name__=="__main__": print(main())    
        

