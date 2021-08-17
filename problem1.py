def sum_multiples(N,divisors):
    total=0
    for i in range(1,N):
        if any(i % d == 0 for d in divisors):
            total+=i
    return total

if __name__=="__main__":
    print(sum_multiples(1000,[3,5]))        
