def isPentagonal(n):
    val=1/6*(1+(1+24*n)**0.5)
    if val.is_integer(): return True
    return False

def isTriangular(n):
    val=1/2*(-1+(1+8*n)**0.5)
    if val.is_integer(): return True
    return False

def isHexagonal(n):
    val=1/4*(1+(1+8*n)**0.5)
    if val.is_integer(): return True
    return False

def Hexagonal(n):
    return n*(2*n-1)

def Triangular(n):
    return n*(n+1)//2

def main():
    i=144
    while True:
        tmp=Hexagonal(i)
        if isPentagonal(tmp):
            return tmp
        i+=1

if __name__=="__main__": 
    print(main())
        
