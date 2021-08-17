def gen_nums(N):
    nums=[]
    for a in range(2,N+1):
        for b in range(2,N+1):
            val=a**b
            if val not in nums:
                nums.append(val)
    return len(nums)

if __name__=="__main__":
    print(gen_nums(100))
