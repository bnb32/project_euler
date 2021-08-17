def champ_digits(N):
    s='0'
    i=1
    while len(s)<N+1:
        s+=str(i)
        i+=1
    digits=[s[1],s[10],s[10**2],s[10**3],s[10**4],s[10**5],s[10**6]]
    prod=1
    for d in digits: prod*=int(d)
    return prod,digits                

if __name__=="__main__":
    print(champ_digits(1000000))
