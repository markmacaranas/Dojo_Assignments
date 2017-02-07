# #Odd/Even
# def odd_even():
#     for x in range(1,2001):
#         if x%2 != 0:
#             print "Number is", x ,"This is an odd number."
#         if x%2 == 0:
#             print "Number is", x ,"This is an even number."
#     return x
# odd_even()

#Multiply
def multiply(arr,num):
    for i in range(len(arr)):
        arr[i] *= num
    return arr
# print multiply([2,4,10,16])

#Hacker Challenge
def hacker_challenge(multiply):
    list = []
    for i in multiply:
        sublist = []
        for num in range(1,i+1):
            sublist.append(1)
            if num == i:
                list.append(sublist)
    print list

hacker_challenge(multiply([2,4,5],3))
