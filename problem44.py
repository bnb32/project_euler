def pent_num(j):
    return j*(3*j-1)//2

def pent_sol(p):
    return (1/6)*(1+(1+24*p)**0.5)

def main():
    searching=True
    nums=[]
    i=1
    while searching:
        num=pent_num(i)
        nums.append(num)
        if nums[-1]-nums[0]>nums[-1]:
            nums.pop()
        for n in nums[:-1]:
            diff=nums[-1]-n
            summa=nums[-1]+n
            if pent_sol(diff).is_integer() and pent_sol(summa).is_integer(): return diff
        i+=1    
            
if __name__=="__main__":
    print(main())
