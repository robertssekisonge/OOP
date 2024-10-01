class university:
    def __init__(self, name, location, motto, years_of_existance,branches=1):
        self.name= name
        self.location=location
        self.motto=motto
        self.years_of_existance= years_of_existance
        self.braches=branches
        
        
        
        
    def __str__(self):    
        return(f"name :{self.name} \nlocation :{self.location}\n motto: {self.motto} \nyears_of_existance: {self.years_of_existance} \nbraches:{self.braches}")
        
        
    
university1 = university("ucu","mukono","centre of excellnce in the heart of africa", 100,4)
university2 = university("mubs","kampala","strive for excellence", 15,2)
university3 = university("kyambogo","banda","lets build the future", 10, 2 )

print(university1)

print(university2)

print(university3)

