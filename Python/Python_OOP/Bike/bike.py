class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        if self.miles < 0:
            self.miles = 0
        print self.price, self.max_speed, self.miles

    def ride(self):
        self.miles += 10
        print "Riding"

    def reverse(self):
        self.miles -= 5
        print "Reversing"

bike1 = Bike(5000,"25mph",0);
bike2 = Bike(6000,"30mph",0);
bike3 = Bike(7000,"35mph",0);

bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
