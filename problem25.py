def fib_nums(N):
    f1=0
    f2=1
    fn=0
    count=1
    while len(str(fn))<N:
        fn=f2+f1
        f1=f2
        f2=fn
        count+=1
    return [count,fn]

if __name__=="__main__":
    print(fib_nums(1000))
