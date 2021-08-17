def divide(N):
    rems=[]
    reps=[]
    tmp=1
    while tmp!=0:
        if tmp not in rems:
            rem=tmp%N
            val=int(10*rem)
            tmp=val%N
            rems.append(rem)
            reps.append(val//N)
        else:
            i=rems.index(tmp)
            reps=reps[i:]
            break
    if tmp!=0:
        return rems,reps
    else:
        return [0],[0]
    
def unit_fracs(N):
    fracs={}
    for n in range(2,N):
        fracs[n]=divide(n)[1]
    return fracs

def max_period(fracs):
    lengths=[len(v) for v in fracs.values()]
    val=max(lengths)
    return lengths.index(val)+2

if __name__=="__main__":
    print(max_period(unit_fracs(1000)))
