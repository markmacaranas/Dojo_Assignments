import random

def coinToss():
    # number = input("Number of times to flip coin:")
    # recordList = []
    heads = 0
    tails = 0
    for x in range (1, 5001):
        flip = random.randint(0, 1)
        if(flip == 0):
            heads += 1
            print("Throwing a coin... It's a head! ... Got " +str(heads)+ " head(s) so far and " +str(tails)+ " tail(s) so far")
        else:
            tails += 1
            print("Throwing a coin... It's a tail! ... Got " +str(heads)+ " head(s) so far and " +str(tails)+ " tail(s) so far")

coinToss()
