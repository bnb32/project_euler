import math

factorials=[math.factorial(i) for i in range(0,10)]

def factorial_digit_sum(n):
    tmp=n
    summa=0
    while tmp:
        summa+=factorials[tmp%10]
        tmp//=10
    return summa

chains={}
def chain_length(n):
    nums=[]
    tmp=n
    while tmp not in nums:
        if tmp in chains: 
            return len(nums)+chains[tmp]
        else:
            nums+=[tmp]
            tmp=factorial_digit_sum(tmp)
    
    chains[n]=len(nums)
    return len(nums)
    
def main():
    N=10**6
    count=0
    for i in range(1,N):
        #print("num: %s"%i)
        if chain_length(i)==60: count+=1
    return count

if __name__=="__main__": print(main())    
