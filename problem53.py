def factorial(n):
    val=1
    for i in range(2,n+1):
        val*=i
    return val

def binomial(n,k):
    return factorial(n)//(factorial(k)*factorial(n-k))

def main():
    count=0
    for n in range(1,101):
        for k in range(2,n//2+1):
            if binomial(n,k)>10**6: 
                if n%2==0 and k==n//2: 
                    count+=1
                else:
                    count+=2
    return count

if __name__=="__main__": print(main())    
