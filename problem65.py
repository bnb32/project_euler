def eulerNums(n):
    nums=[]
    for i in range(0,n):
        if i==0: nums.append(2)
        else:
            k=(i+1)//3
            if (i+1) % 3 == 0: nums.append(2*k)
            else: nums.append(1)
    return nums    

def simplifyFrac(numer,denom,num):
    n=denom*num+numer
    d=denom
    return [n,d]

def getConvergent(nums):
    denom=nums[-1]
    numer=1
    for i in range(len(nums)-2,-1,-1):
        [denom,numer]=simplifyFrac(numer,denom,nums[i])
    return [denom,numer]

def main():
    nums=eulerNums(100)
    [n,d]=getConvergent(nums)
    return sum([int(d) for d in str(n)])

if __name__=="__main__": print(main())    
