def pythag_triple(m,n):
    a=(m*m)-(n*n)
    b=2*m*n
    c=(m*m)+(n*n)
    return [a,b,c]

def pythag_product(N):
    tmp=0
    for i in range(1,N):
        for j in range(i+1,N+1):
            vals=pythag_triple(j,i)
            if sum(vals)==1000:
                return vals[0]*vals[1]*vals[2]


if __name__=="__main__":
    print(pythag_product(25))
