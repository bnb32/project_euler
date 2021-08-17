def main():
    tmp=28433
    for i in range(0,7830457):
        tmp<<=1
        tmp%=10**10
    return (tmp+1) % 10**10

print(main())    
