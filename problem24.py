import math

def perm_string(nums):
    s=''
    for i in range(0,len(nums)):
        s+=str(nums[i])
    return s    

def permutations(nums):
    perms=[]
    for n in nums:
        perms.append([n])

    for count in range(1,len(nums)):    
        tmp=[]
        for p in perms:
            for n in nums:
                if n not in p:
                    tmp.append(p+[n])
        perms=tmp
    
    return perms

perms=permutations([0,1,2,3,4,5,6,7,8,9])
print(perm_string(perms[10**6-1]))
