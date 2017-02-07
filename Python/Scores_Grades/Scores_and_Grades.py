import random

def random1():
    random_score = random.randrange(60,101)
    return random_score

def random_grades():
    for i in range(0,10):
        score = random1()
        if score >= 90:
            print "Score", str(score) + " Your grade is A"
        elif score >= 80:
            print "Score", str(score) + " Your grade is B"
        elif score >=70:
            print "Score", str(score) + " Your grade is C"
        elif score >= 60:
            print "Score", str(score) + " Your grade is D"



random_grades()
