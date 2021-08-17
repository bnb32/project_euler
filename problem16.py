def power_sum(N):
    nums=str(N)
    tmp=0
    for n in nums:
        tmp+=int(n)
    return tmp

if __name__=="__main__":
    print(power_sum(2**1000))
