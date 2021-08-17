import euler_project as euler

@euler.memoize
def partitions(n,m):
    if m<1 or n<1: return 0
    elif m==n: return 1+partitions(n,m-1)
    elif m==1: return 1
    else:
        return partitions(n,m-1)+partitions(n-m,m)


if __name__=="__main__": print(partitions(100,99))    
        
    
