def formula(a,b,c):
    if a*(10*b-9*c)==b*c and a!=c:
        return [10*a+b,10*b+c,a,c]
    return False

if __name__=="__main__":
    numerator=1
    denominator=1
    for a in range(1,10):
        for b in range(1,10):
            for c in range(1,10):
                f=formula(a,b,c)
                if f!=False:
                    numerator*=f[2]
                    denominator*=f[3]
    if denominator % numerator == 0:
        denominator//=numerator
        numerator=1
    print("%s/%s"%(numerator,denominator))
                
        
