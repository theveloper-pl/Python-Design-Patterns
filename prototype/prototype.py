import copy

class CarPrototype:
    def clone(self, VIN, **kwargs):
        """
        Clone the current object deeply and update its attributes,
        including a new VIN.
        """
        new_car = copy.deepcopy(self)
        new_car.VIN = VIN
        new_car.__dict__.update(kwargs)
        return new_car

    def shallow_clone(self, VIN, **kwargs):
        """
        Shallowly clone the current object and update its attributes,
        including a new VIN.
        """
        new_car = copy.copy(self)
        new_car.VIN = VIN
        new_car.__dict__.update(kwargs)
        return new_car

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def __str__(self):
        return f"Engine type: {self.engine_type}"

class Car(CarPrototype):
    def __init__(self, VIN, model, color, production_year, engine):
        self.VIN = VIN
        self.model = model
        self.color = color
        self.production_year = production_year
        self.engine = engine

    def __str__(self):
        return f"""VIN: {self.VIN}, Model: {self.model}, \
Color: {self.color}, Production Year: {self.production_year}, \
{self.engine}"""

if __name__ == "__main__":
	car_engine = Engine("V-type")
	car = Car("1HGCM82633A1234", "Civic", "Red", "2023", car_engine)

	shallow_copied_car = car.shallow_clone("HSBV82NSJBVI23S")
	deep_copied_car = car.clone("ZKLK2MVIOJSJSDO")

	print(car)
	print(shallow_copied_car)
	print(deep_copied_car)

	print(car.engine is shallow_copied_car.engine) # Car and shallow_copied car share the same engine isntance
	print(car.engine is deep_copied_car.engine) # Both Car and Deep copied car have own engine instance