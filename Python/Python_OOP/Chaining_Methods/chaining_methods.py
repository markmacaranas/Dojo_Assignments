class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        if self.miles < 0:
            self.miles = 0
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        self.miles += 10
        print "Riding"
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing"
        return self

bike1 = Bike(5000,"25mph",0);
bike2 = Bike(6000,"30mph",0);
bike3 = Bike(7000,"35mph",0);

bike1.ride().ride().ride().reverse().displayInfo()

bike2.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()
