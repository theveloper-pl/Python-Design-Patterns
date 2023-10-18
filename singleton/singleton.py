class Singleton:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print("No instance found. Creating new instance!")
            print(cls.__dict__)
            cls.instance = super(Singleton, cls).__new__(cls)
        else:
            print(cls.__dict__)
            print("Instance already exists")
          
        print("Returning instance")
        return cls.instance

print("\n\nCreating first object")
first_singleton_obj = Singleton()

print("\n\nSecond object creation")
second_singleton_obj = Singleton()

print("\n\nAre first and second objects the same:", 
        first_singleton_obj is second_singleton_obj)

first_singleton_obj.name = "Singleton Variable"
print("First obj variable:", first_singleton_obj.name)
print("Second obj variable:", second_singleton_obj.name)
