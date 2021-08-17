def isNdigits(m,n):
    if len(str(m))==n: return True
    return False

def main():
    count=1
    N=1
    while len(str(9**N))>=N:
        for i in range(2,10):
            if isNdigits(i**N,N): count+=1
        N+=1    
    return count      

if __name__=="__main__": print(main())
