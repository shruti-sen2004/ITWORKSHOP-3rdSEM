from abc import ABC, abstractmethod
class Vehicle(ABC): # Define the Abstract Base Class
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    @abstractmethod
    def drive(self):
        pass

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

class Car(Vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} on four wheels")

class Bike(Vehicle):
    def drive(self):
        print(f"Driving the {self.make} {self.model} on two wheels")

my_car = Car("Ford", "Focus")
my_bike = Bike("Kawasaki", "Ninja")
my_car.drive()
my_car.stop()
my_bike.drive()
my_bike.stop()
# my_vehicle = Vehicle("Generic", "Vehicle") # abstract class cannot be instantiated with abstract method

# An ABC acting as an Interface
# ABC containg only abstracts methods 
# Works similar to interface in java or c++
class Logger(ABC):
    @abstractmethod
    def log_info(self, message):
        pass

    # @abstractmethod
    # def log_error(self, message):
    #     pass

class Register(Logger): # must have all the abstract classes declared here
    def __init__(self):
        super().__init__("Register1")
    def log_info(self, message):
        print(f"{message} has logged in")
