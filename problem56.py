def digit_sum(N):
    summa=0
    for d in str(N): summa+=int(d)
    return summa

def main():
    sums=[]
    for a in range(1,100):
        for b in range(1,100):
            sums.append(digit_sum(a**b))
    return max(sums)

if __name__=="__main__":
    print(main())
