def prime_factor(N):
    i=2
    while i*i <= N:
       if N % i == 0:
           N//=i
       else:
           i+=1
    return N

def prime_factors(N):
    divs=[prime_factor(N)]
    if divs[-1]==N: return []
    while divs[-1]!=N:
        N//=divs[-1]
        divs.append(prime_factor(N))
    return divs    

def unique(nums):
    unique=[]
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique    

def main():
    nums=[]
    i=1
    while len(nums)<4:
       if len(unique(prime_factors(i)))==4:
           for j,n in enumerate(nums[::-1].copy()):
               if n!=i-j-1: nums.pop(-1)
           nums.append(i)
       i+=1
    return nums

if __name__=="__main__": print(main())    

