import euler_project as euler

@euler.memoize
def closest_fraction(n):
    numerator=(3*n-1)/7
    if numerator % 1 != 0: return []
    else: return ["%s/%s"%(int(numerator),n)]

def all_close_fractions(n,m):
    nums=["3/7"]
    for i in range(m,n+1):
        nums+=closest_fraction(i)
    nums.sort(key=fraction_decimal)
    
    return nums    

def fraction_decimal(elem):
    tmp=elem.split('/')
    return float(tmp[0])/float(tmp[1])

def main():
    N=10**6
    M=2
    fractions=all_close_fractions(N,M)
    idx=fractions.index("3/7")
    return fractions[idx-1]

if __name__=="__main__": 
    print(main())
