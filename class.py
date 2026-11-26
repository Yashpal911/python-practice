class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model
        
    def fullname(self):
        return f"{self.model} of {self.brand} Brand"


class ElectricCar(Car):
    def __init__(self, model, brand, battery):
        super().__init__(model, brand)
        self.battery = battery

    def fullname(self):
        return super().fullname() + f"with {self.battery}"
    
# print(Car("alto","maruti").brand)
# print(Car("alto","maruti").model)
# print(Car("alto","maruti").fullname().capitalize())


print(ElectricCar('alto', 'maruti', 'no battery').fullname())
print(Car('alto', 'maruti').fullname())