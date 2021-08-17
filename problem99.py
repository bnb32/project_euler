import math

def main():
    nums=[]
    f=open('./p099_base_exp.txt','r')
    for l in f.readlines():
        nums.append(l.strip('\n').split(','))
    prod=0
    line=0
    for i,num in enumerate(nums):
        tmp=int(num[1])*math.log(int(num[0]))
        if tmp>prod:
            prod=tmp
            line=i+1
    return nums[line-1],line

print(main())    
