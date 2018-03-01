fiblist = [1,2]
evenfiblist = []
a = 0
i = 0

while fiblist[i] < 4000000:
    if fiblist[i+1]%2 ==0:
        evenfiblist.append(fiblist[i+1])
        print evenfiblist
        a += fiblist[i+1]
    fiblist.append(fiblist[i] + fiblist[i+1])
    i += 1
    
print a, '\n\,evenfiblist

