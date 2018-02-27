total = 0
for i in range(1,100):
    if i%3 == 0 or i%5 ==0:
        total += i
print total 


sum = 0
i = 0
list1 = list(range(1, 100))
while i < len(list1): 
    if list1[i]%3 == 0 or list1[i]%5 == 0:
        sum += list1[i]
    i += 1
print sum

