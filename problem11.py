f=open('./problem11.txt','r')
grid=[]
for l in f.readlines():
    grid.append(l.split())

def dig_product(x):
    tmp=1
    for d in x:
        tmp*=int(d)
    return tmp    

def grid_product():
    prods=[]
    for i in range(0,20):
        for j in range(0,20):
            #horizontal
            if j+3<20:
                tmp=[grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3]]
                prods.append(dig_product(tmp))
            #vertical
            if i+3<20:
                tmp=[grid[i][j],grid[i+1][j],grid[i+2][j],grid[i+3][j]]
                prods.append(dig_product(tmp))
            #diag down-right
            if i+3<20 and j+3<20:
                tmp=[grid[i][j],grid[i+1][j+1],grid[i+2][j+2],grid[i+3][j+3]]
                prods.append(dig_product(tmp))
            #diag up-right
            if i+3<20 and j-3>=0:
                tmp=[grid[i][j],grid[i+1][j-1],grid[i+2][j-2],grid[i+3][j-3]]
                prods.append(dig_product(tmp))
    return max(prods)

if __name__=="__main__":
    print(grid_product())

