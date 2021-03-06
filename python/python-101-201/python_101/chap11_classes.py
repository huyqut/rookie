# CLASSES


class Thing:

    def run(self):
        print("This is the thing")


class Vehicle(Thing):
    """A class of vehicle"""

    ground = True  # Static variable (can be "personalized" if an object changes this variable itself)

    def __init__(self, wheels, color, speed, seats):
        """Constructor"""
        # Attributes of an object inside class
        self.wheels = wheels
        self.color = color
        self.speed = speed
        self.seats = seats
        self.start = False

    def run(self):
        """Method to run a vehicle"""
        super(Vehicle, self).run()
        self.start = True
        print("Dude! I'm here")

    def _private_mate(self):
        print("This method does not prevent being called from outside but indicates that it should not be called.")
        self.speed = 1000

    def roar(self):
        print("I'm Super!!!")
        self.__should_not_override()

    def __should_not_override(self):  # Name is changed, cannot be called from outside
        """
        Convention: The __method_name will be changed to _class__method_name => Can only invoked from inside
        __method_name_ can also be applied (at MOST 1 trailing underscore is allowed)
        """
        print("super cool!")

vehicle = Vehicle(4, 'black', 100, 8)  # Initialize a class
print(type(vehicle))
print(f"{vehicle.ground} - {Vehicle.ground}")  # At this stage, everything is still the same
vehicle.ground = False
print(f"{vehicle.ground} - {Vehicle.ground}")  # "vehicle" object makes its own "ground", not relating to Vehicle.ground

# __method__ should never be user-defined. Only use from the docs only.

print(vehicle.__doc__)  # Docstring
print(vehicle.__hash__())  # Hash of the object


# _method_like_this can still be invoked outside of the class scope but it should NOT be called.
vehicle._private_mate()


class Car(Vehicle):  # Inherit from Vehicle
    """This is a subclass of Vehicle"""

    def roar(self):
        super().roar()
        print("This is Suber!!!")
        self.__should_not_override()

    def __should_not_override(self):  # It does not override super method because it cannot call that method
        print('This should happen')


car = Car(1, 2, 3, 4)
car.roar()


# Multiple inheritance

class Animal(Thing):
    """Animal class"""

    def __init__(self, blood, eyes):
        self.blood = blood
        self.eyes = eyes

    def run(self):
        super(Animal, self).run()
        print("Woohoo!!!")


class Horse(Animal, Vehicle):  # If there is not constructor, it choose the 1st super as default constructor
    """A horse can be an animal and a vehicle"""

    def run(self):
        super(Horse, self).run()  # super solves the diamond problem
        print("Done man")  # Done here

horse = Horse('red', 4)
horse.run()

# Examples of using BaseClass.method() instead of calling super()


class A:

    def do(self):
        print("A run")


class B(A):

    def do(self):
        A.do(self)
        print("B run")


class C(A):

    def do(self):
        A.do(self)
        print("C run")


class D(B, C):

    def do(self):
        # This will duplicate A
        B.do(self)
        C.do(self)
        print("D run")

        # This will only use the 1st class declared on D: A B D
        print()
        super().do()
        print("D run")

        # Use super as above for Thing, Vehicle, Animal and Horse to solve diamond problem.

D().do()
