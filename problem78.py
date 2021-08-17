import euler_project as euler
from collections import defaultdict

stored_partitions=defaultdict(int)
stored_pentagonal_partitions=defaultdict(int)

def pentagonal_partitions(n):
    i=2
    nums=[n-1]
    while nums[-1]>0:
        nums.append(n-euler.GeneralizedPent(i))
        i+=1
    summa=0
    for i,n in enumerate(nums):
        tmp=stored_pentagonal_partitions[n]
        if tmp>0: 
            pass
        else:
            tmp=partitions(n,n)
        if i%4==0 or i%4==1: 
            summa+=tmp
        else: 
            summa-=tmp
    return summa    
        
#@euler.memoize
def partitions(n,m):
    if m==1 or n==1: return 1
    if n==0: return 1
    if n<0: return 0
    if stored_partitions[(n,m)]!=0:
        return stored_partitions[(n,m)]
    summa=0
    for i in range(m,0,-1):
        if stored_partitions[(n-i,i)]!=0:
            summa+=stored_partitions[(n-i,i)]
        else:
            summa+=partitions(n-i,i)
    stored_partitions[(n,m)]=summa
    return summa    

for n in range(2,10**5):
    num=pentagonal_partitions(n)
    print("n: %s" %(n))
    #print("n,count: %s,%s" %(n,num))
    #print("stored length: %s" %(len(stored_pentagonal_partitions)))
    if num % 10**6 == 0:
        print(n)
        break
