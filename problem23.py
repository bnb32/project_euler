import math

def factors(N):
    divs=[1]
    for n in range(2,int(math.sqrt(N))+1):
        if N % n == 0: 
            divs.append(n)
            if N/n!=n:
                divs.append(N//n)

    return divs

def abundant_nums(N):
    return [n for n in range(1,N+1) if sum(factors(n))>n]

def sum_check(N,nums):
    i=0
    j=len(nums)-1
    while j>=i:
        if nums[j]+nums[i]>N: j-=1
        elif nums[j]+nums[i]<N: i+=1
        else: return True
    return False            

def non_sum(N,nums):
    val=0
    for i in range(1,N+1):
        if not sum_check(i,nums):
            val+=i
    return val

if __name__=="__main__":
    nums=abundant_nums(28123)
    print(non_sum(28123,nums))
    #print(factors(24))

