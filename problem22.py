scores={'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,
        'o':15,
        'p':16,
        'q':17,
        'r':18,
        's':19,
        't':20,
        'u':21,
        'v':22,
        'w':23,
        'x':24,
        'y':25,
        'z':26}


def score_names(names):
    names.sort()
    sums=0
    for i,name in enumerate(names):
        sums+=(i+1)*(sum([scores[n] for n in name.lower().strip('"')]))
    return sums

if __name__=="__main__":
    f=open('./p022_names.txt','r')
    names=list(f.readline().split(','))
    print(score_names(names))
