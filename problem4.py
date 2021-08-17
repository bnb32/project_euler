def palindrome(N):
    tmp=[]
    for i in range(10**(N-1),10**N):
        for j in range(i+1,10**N):
            num=i*j
            if str(num)==str(num)[::-1]:
                tmp.append(num)
    return max(tmp),len(tmp)

if __name__=="__main__":
    print(palindrome(3))
