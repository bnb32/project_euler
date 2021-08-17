def div_sum(N):
    divs=[]
    for n in range(1,N//2+1):
        if N % n == 0:
            divs.append(n)
    return sum(divs)


def all_div_sums(N):
    div_sums={}
    for i in range(1,N):
        div_sums[i]=div_sum(i)
    return div_sums

def amicable_check(N,div_sums):
    if div_sums[N] in div_sums:
        if div_sums[div_sums[N]]==N and div_sums[N]!=N:
            return True
    return False        

def amicable_sum(div_sums):
    sums=0
    for n in div_sums.keys():
        if amicable_check(n,div_sums):
            sums+=n
    return sums

if __name__=="__main__":
    div_sums=all_div_sums(10000)
    print(amicable_sum(div_sums))
    
