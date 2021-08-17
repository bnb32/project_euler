import euler_project as euler
import itertools


def getNums(func,N):
    nums=[];n=1;tmp=func(n)
    while tmp<10**(N-1): 
        n+=1
        tmp=func(n)
    while 10**(N-1)<=tmp<10**N:
        nums.append(tmp)
        n+=1
        tmp=func(n)
    return nums    

def nextNum(num,nums):
    poss=[]
    for n in nums:
        if str(n)[0:2]==str(num)[2:4] or str(n)[2:4]==str(num)[0:2]: poss.append(n)
    return poss

def isCyclic(nums):
    n0=nums[0];n1=nums[1];n2=nums[2];n3=nums[3];n4=nums[4];n5=nums[5]
    if isMatch(n0,n1) and isMatch(n1,n2) and isMatch(n2,n3) and isMatch(n3,n4) and isMatch(n4,n5) and isMatch(n5,n0): return True
    return False

@euler.memoize
def isMatch(n,m):
    if str(n)[2:4]==str(m)[0:2]: return True
    return False

def walkNums(all_nums,order):
    for n0 in all_nums[order[0]]:
      for n1 in all_nums[order[1]]:
        if isMatch(n0,n1):
          for n2 in all_nums[order[2]]:
            if isMatch(n1,n2):
              for n3 in all_nums[order[3]]:
                if isMatch(n2,n3):
                  for n4 in all_nums[order[4]]:
                    if isMatch(n3,n4):
                      for n5 in all_nums[order[5]]:
                        if isMatch(n4,n5) and isMatch(n5,n0):
                          tmp=[n0,n1,n2,n3,n4,n5]
                          return tmp,[r+3 for r in order],sum(tmp)
    return False

def main():
    N=4
    tris=getNums(euler.Tri,N)
    squares=getNums(euler.Square,N)
    pents=getNums(euler.Pent,N)
    hexs=getNums(euler.Hex,N)
    hepts=getNums(euler.Hept,N)
    octs=getNums(euler.Oct,N)
    all_nums=[tris,squares,pents,hexs,hepts,octs]

    perms=itertools.permutations([0,1,2,3,4,5],6)
    for p in perms:
        tmp=walkNums(all_nums,p)
        if tmp!=False: return tmp

    return None

if __name__=="__main__": print(main())                   
