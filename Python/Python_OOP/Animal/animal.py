import random

class Animal(object):                       #define the Animal class
    def __init__(self, name, health=100):       #define a parameter with a default value: self and name, health attributes
        #define attributes
        self.name = name
        self.health = health
    print 'I am an animal!'

    def walk(self):
        self.health -= 1
        # print "Walking!" #for testing
        return self

    def run(self):
        self.health -= 5
        # print "Running!" #for testing
        return self

    def displayHealth(self):
        print self.name, self.health
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)      #use super to call the Animal __init__method
        self.health = 150

    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)     #use super to call Animal __init__method
        self.health = 170

    def displayHealth(self):
        print "this is a dragon!"
        super(Dragon, self).displayHealth()

    def fly(self):
        self.health -= 10
        return self

animal = Animal("animal")
dog = Dog('dog')
dragon = Dragon('dragon')

animal.walk().walk().walk().run().run().displayHealth()
dog.walk().walk().walk().run().run().pet().displayHealth()
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
