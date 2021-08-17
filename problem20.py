import math

def fac_dig_sum(N):
    num=math.factorial(N)
    return sum(int(n) for n in str(num))

if __name__=="__main__":
    print(fac_dig_sum(100))
