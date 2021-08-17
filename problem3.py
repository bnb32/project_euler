def prime_factor(N):
    i=2
    while i*i <= N:
       if N % i == 0:
           N//=i
       else:
           i+=1
    return N

if __name__=="__main__":
    print(prime_factor(600851475143))
