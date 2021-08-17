import euler_project as euler

@euler.memoize
def farley_series_length(n):
    return sum([euler.euler_totient(i) for i in range(2,n+1)])

def main():
    N=10**6
    return farley_series_length(N)    

if __name__=="__main__":
    print(main())    
