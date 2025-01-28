class Car:
    #constructor self means this current obj
    def __init__(self, model, year,color,sale):
        self.model=model
        self.year=year
        self.color=color
        self.sale=sale

    def drive(self):
        print(f"You drive the car of model{self.color} {self.model}")
    def stop(self):
        print(f"You stop the{self.color} {self.model}")

    def describe(self):
        print(f"The cars description is a {self.color} {self.model} from  {self.year}")