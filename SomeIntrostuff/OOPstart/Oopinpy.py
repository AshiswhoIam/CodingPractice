from CarClass import Car
        
car1= Car("Spider",2025,"Blue",False)
car2= Car("Civic",2015,"Black",True)
car3= Car("Corolla",2005,"Red",True)
#print(car1) would give the memo address
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.sale)

car1.drive()
car2.stop()
car3.describe()