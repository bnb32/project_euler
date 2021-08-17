import itertools
from collections import defaultdict

def magic_ngon(nums):
    branches=len(nums)//2
  
    combos=[[nums[0],nums[1],nums[2]]]
    for i in range(1,branches):
        tmp=[nums[2*i+1],nums[2*i]]
        if i==branches-1: tmp.append(nums[1])
        else: tmp.append(nums[2*(i+1)])
        combos.append(tmp)
    return combos    

def is_ngon_solution(combos):
    summa=sum(combos[0])
    if not all(combos[0][0]<combos[i][0] for i in range(1,len(combos))): return False
    
    if all(sum(combos[i])==summa for i in range(1,len(combos))): return True
    return False

def graph_permutations(n):
    perms=itertools.permutations([i for i in range(1,n+1)])
    return [p for p in perms]

def join_combo(c):
    s=''
    for b in c:
        for n in b: s+=str(n)
    return s

def main():
    perms=graph_permutations(10)
    nums=[]
    for p in perms:
        c=magic_ngon(p)
        if is_ngon_solution(c): 
            s=join_combo(c)
            if len(s)==16: nums.append(int(s))
    return max(nums)

if __name__=="__main__": print(main())    
