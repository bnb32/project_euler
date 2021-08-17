denoms={}
numers={}

def numerator(n):
    if n==0:
        return 1
    else:
        if (n-1) in denoms: 
            denom=denoms[n-1]
        else:
            denom=denominator(n-1)
            denoms[n-1]=denom
        if (n-1) in numers:
            numer=numers[n-1]
        else:
            numer=numerator(n-1)
            numers[n-1]=numer
        return 2*denom+numer

def denominator(n):
    if n==0:
        return 1
    else:
        if (n-1) in denoms: 
            denom=denoms[n-1]
        else:
            denom=denominator(n-1)
            denoms[n-1]=denom
        if (n-1) in numers:
            numer=numers[n-1]
        else:
            numer=numerator(n-1)
            numers[n-1]=numer
        return denom+numer

def main():
    count=0
    for i in range(1,1001):
        numer=numerator(i)
        denom=denominator(i)
        if len(str(numer))>len(str(denom)): count+=1
    return count

if __name__=="__main__": print(main())    
