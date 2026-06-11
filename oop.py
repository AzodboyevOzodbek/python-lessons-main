# oop - object-oriented programming
# 1.class(xususiyatlari, metodlari) va object
# 2.oop ustunlari
    # 1.Encapsulation - kapsulalash
    # 2.Inheritance - meros olish
    # 3.Polymorphism - ko'p shakllilik
    # 4.Abstraction - abstraksiya

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def yur(self):
        print(f"{self.model} yuryabdi")

    def toxta(self):
        print(f"{self.model} to'xtadi.")

# objects
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)

car1.yur()
car2.yur()
car1.toxta()
car2.toxta()