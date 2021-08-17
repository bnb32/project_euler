import math

def candidates(n0,n1):
    nums=[]
    for i in range(n0,n1):
        if len(str(i))==len(set(str(i))):
            nums.append(i)
    return nums

def factors(N):
    for i in range(2,int(math.sqrt(N))):
        if N % i == 0:
            nums=str(i)+str(N//i)+str(N)
            if len(nums)==9 and len(set(nums))==9 and '0' not in nums:
                return True
    return False

if __name__=="__main__":
    nums=candidates(10**2,10**5)
    val=0
    for n in nums:
        if factors(n):
            val+=n
    print(val)        
