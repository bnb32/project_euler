def square_difference(N):
    a=N*N*(N+1)*(N+1)//4
    b=N*(N+1)*(2*N+1)//6
    return a-b

if __name__=="__main__":
    print(square_difference(100))    
