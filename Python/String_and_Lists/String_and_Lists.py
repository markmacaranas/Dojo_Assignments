#Find and Replace
animal = "monkey"
phrase = "If {} like bananas, then I must be a {}".format(animal,animal)
print phrase

#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[7]

y = [x[0], x[-1]]
print y

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
# how to sort list ascending

new_x = [y for y in x if y<0]
#if item in a for loop; y is the item; x is the variable; y < 0 is the statement)
print new_x

x.pop(0)
x.pop(0)
print x

x.insert(0,new_x)
print x
