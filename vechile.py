class Vehicle:
    
    
    def __init__(self, color, name):
        self.color = color
        self.name=name
    def get_color(self):
        return self.color

    def __str__(self):
        return f"This vehicle is {self.color}"
    


 
my_vehicle = Vehicle("red")


print(my_vehicle.get_color()) 


print(my_vehicle)  
