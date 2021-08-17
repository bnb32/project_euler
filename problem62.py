import itertools
import euler_project as euler

def joinDigits(p):
    s=[str(d) for d in p]
    s=''.join(s)
    return int(s)

def cubeRange(nums):
    min_num=nums
    min_num.sort()
    max_num=min_num[::-1]
    i=0
    if min_num.count(0)>0:
        while min_num[i]==0: i+=1
        min_num=[min_num[i]]+min_num[0:i]+min_num[i+1:]
    return [int(joinDigits(min_num)**(1/3)),int(joinDigits(max_num)**(1/3))+1]    

def getDigits(num):
    return [int(d) for d in str(num)]

def countCubes(num):
    nums=getDigits(num)
    [nmin,nmax]=cubeRange(nums)
    nums.sort()
    count=0
    for n in range(nmin,nmax+1):
        num=n**3
        ds=getDigits(num)
        ds.sort()
        if ds==nums: count+=1
    return count    

def main():
    n=2
    N=5
    while True:
        num=n**3
        if countCubes(num)==N: return num
        n+=1

if __name__=="__main__": 
    print(main())
