def cat_nums(n):
    s=''
    i=1
    while len(s)<9:
       s+=str(i*n)
       i+=1
    for d in s:
        if s.count(d)>1 or d=='0': return False
    return s

def main():
    for n in range(10**4,1,-1):
        s=cat_nums(n)
        if s!=False: return s

if __name__=="__main__":
    print(main())
