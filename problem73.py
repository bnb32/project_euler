import euler_project as euler
import math

def farley_length_in_range(f_min,f_max,d):
    nums=[i for i in range(int(d*f_min),int(d*f_max)+1) if f_min<i/d<f_max and math.gcd(i,d)==1]
    return len(nums)


def main():
    N=12000
    summa=0
    for i in range(2,N+1):
        val=farley_length_in_range(1/3,1/2,i)
        summa+=val
    return summa

if __name__=="__main__":
    print(main())    
    
