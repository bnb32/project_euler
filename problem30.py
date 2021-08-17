def digit_sum(N,p):
    tmp=0
    for n in str(N):
        tmp+=int(n)**p
    return tmp 

def sum_check(N,p):
    if digit_sum(N,p)==N: 
        return True
    return False

if __name__=="__main__":
    val=0
    for i in range(10**2,10**6):
        tmp=digit_sum(i,5)
        if tmp==i: val+=tmp
    print(val)    
