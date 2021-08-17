months={1:31,2:[28,29],3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

def isLeap(num):
    if num % 100 != 0 and num % 4 == 0:
        return True
    elif num % 100 == 0 and num % 400 == 0:
        return True
    else:
        return False

def isSunday(num):
    #days since starting monday
    if (num+1) % 7 == 0:
        return True
    else:
        return False

def firstSundays():
    sundays=0
    days=0
    for year in range(1900,2001):
        for i in range(1,13):
            if isSunday(days) and year>1900:
                sundays+=1
            if i==2 and isLeap(year):
                days+=months[2][1]
            elif i==2:
                days+=months[2][0]
            else:
                days+=months[i]
    return sundays

if __name__=="__main__":
    print(firstSundays())
