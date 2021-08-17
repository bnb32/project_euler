import math

def sum_check(p):
    count=0
    p_frac=1.0/(2+math.sqrt(2))
    for a in range(1,int(p*p_frac)):
        if ((p-a)**2-a**2) % (2*(p-a)) == 0:
            count+=1
    return count

def main():
    val=0
    count=0
    for p in range(1,10**3):
        tmp=sum_check(p)
        if tmp>count:
            count=tmp
            val=p
    return val,count

if __name__=="__main__":
    print(main())
