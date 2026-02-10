class Car:
   

    def __init__(self,make,model,year,color,Owner):
        self.make = make
        self.model= model
        self.year=year
        self.color= color
        self.Owner= Owner 

    def assignOwner(self):
        if self.Owner != None:
            print(f"This is the owner {self}")


