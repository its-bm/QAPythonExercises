# 1)Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
veh = Vehicle(180, 90000)
print(veh.max_speed, veh.mileage)

# 2) Create a Vehicle class without any variables and methods
class Vehicle:
    pass

# 3) Create a child class Bus that will inherit all of the variables and methods of the 1st Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass
big_bus = Bus('Arriva', '80', '342943')
print('Bus name:', big_bus.name, '\nMax speed:', big_bus.max_speed, '\nMileage:', big_bus.mileage)

# 4) Create a Bus object that will inherit all of the variables and methods of the Vehicle class and display it.


# 5) Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Bus(Vehicle):
    
    def seating_capacity(self, capacity = 50):
        return 'Seating capacity:', capacity

Bus.seating_capacity

# 6) Define property that should have the same value for every class instance
# (Define a class attribute”colour” with a default value white)
class Vehicle:
    colour = 'white'
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

Bus.colour

#7) Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is seating capacity * 100.
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#Note: The bus seating capacity is 50. so the final fare amount should be 5500.
# You need to override the fare() method of a Vehicle class in Bus class.
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        fare_final= self.capacity * 100 
        total_fare = fare_final + (0.1 * fare_final)
        return total_fare

big_bus = Bus("Arriva", 342943, 50)
print("Total amount:", big_bus.fare())