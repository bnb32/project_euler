def fib_sum(N):
    total=0
    fib_m1=1
    fib_m2=0
    for i in range(1,N):
        fib=fib_m2+fib_m1
        fib_m2=fib_m1
        fib_m1=fib
        if fib % 2 == 0:
            if total>N: 
                return total
            else:
                total+=fib

if __name__=="__main__":
    print(fib_sum(4*10**6))
