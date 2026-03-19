# 6. Vehicle System
# Create:
#  Base class:
# o Vehicle → attributes: speed, fuel_type
#  Derived classes:
# o Car
# o Bike
# Tasks:
# 1. Implement inheritance structure.
# 2. Demonstrate how code reusability is achieved.
# 3. Show how new features can be added in derived classes


#  using Has-A realtion


class vehicle:
    def __init__(self,speed, fuel_type):
        self.speed = speed
        self.fuel_type = fuel_type

class car:
    def __init__(self,brand_name,v_info):
        self.brand_name = brand_name
        self.v_info  = v_info
    def start(self):
        print(f"car is start with {self.v_info.speed} and have fuel type is {self.v_info.fuel_type}")   

class bike:
    def __init__(self,brand_name,v_info):
        self.brand_name = brand_name
        self.v_info  = v_info  
    def start(self):
        print(f"Bike is start with {self.v_info.speed} and have fuel type is {self.v_info.fuel_type}")   

v1 = vehicle(120,"petrol")

c1 = car("hundai",v1)

c1.start()

b1 = bike("r15",v1)

b1.start()

