# #Multiples Part 1
for count in range(1,1001):
    if count % 2 != 0:
        print count

#Multiples Part 2
for count in range(5,1000001):
    if count % 5 == 0:
        print count

#Sum List
a = [1, 2 ,5, 10, 255, 3]
sum = 0
for x in a:
    sum += x
    print sum

#Assignment: Average List
a = [1, 2 ,5, 10, 255, 3]
sum = 0
for x in a:
    sum += x
    print sum/len(a)
