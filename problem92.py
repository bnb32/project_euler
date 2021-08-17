def add_squared_digits(n):
    return sum([int(d)**2 for d in str(n)])

def main():
    N=10**7
    count=0
    for n in range(1,N):
        num=n
        while num!=89 and num!=1:
            num=add_squared_digits(num)
        if num==89: 
            count+=1
    return count

print(main())
