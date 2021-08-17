from euler_project import isPrime

nums={}
def corner_nums(N):
    if N==1: return [1]
    elif N in nums:
        return nums[N]
    elif (N-2) in nums:
        start=nums[N-2][-1]+(N-1)
    else:
        nums[N-2]=corner_nums(N-2)
        start=nums[N-2][-1]+(N-1)

    return [start+(N-1)*i for i in range(0,4)]

def count_primes(nums):
    count=0
    for n in nums:
        if isPrime(n): count+=1
    return count    

def main():
    n=3
    primes=0
    total=1
    while primes==0 or primes/total > 0.1:
        total+=4
        primes+=count_primes(corner_nums(n))
        n+=2
    return n-2

if __name__=="__main__": print(main())    
