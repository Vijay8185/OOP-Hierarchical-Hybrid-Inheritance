
# Hierarchical inheritance:
# When we derive or inherit more than one child class from one(same) parent class.
# Then this type of inheritance is called hierarchical inheritance.
# Ex.1
class Brands:
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"

class Products(Brands):
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"


class Popularity(Brands):
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60


class Value(Brands):
    prod_1_value = "Excellent Value"
    prod_2_value = "Better Value"
    prod_3_value = "Good Value"


obj_1 = Products()
obj_2 = Popularity()
obj_3 = Value()
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1)
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1)
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1)

# Ex.2
class Details:
    def __init__(self):
        self.__id="<No Id>"
        self.__name="<No Name>"
        self.__gender="<No Gender>"
    def setData(self,id,name,gender):
        self.__id=id
        self.__name=name
        self.__gender=gender
    def showData(self):
        print("Id: ",self.__id)
        print("Name: ", self.__name)
        print("Gender: ", self.__gender)

class Employee(Details): #Inheritance
    def __init__(self):
        self.__company="<No Company>"
        self.__dept="<No Dept>"
    def setEmployee(self,id,name,gender,comp,dept):
        self.setData(id,name,gender)
        self.__company=comp
        self.__dept=dept
    def showEmployee(self):
        self.showData()
        print("Company: ", self.__company)
        print("Department: ", self.__dept)

class Doctor(Details): #Inheritance
    def __init__(self):
        self.__hospital="<No Hospital>"
        self.__dept="<No Dept>"
    def setEmployee(self,id,name,gender,hos,dept):
        self.setData(id,name,gender)
        self.__hospital=hos
        self.__dept=dept
    def showEmployee(self):
        self.showData()
        print("Hospital: ", self.__hospital)
        print("Department: ", self.__dept)

def main():
    print("Employee Object")
    e=Employee()
    e.setEmployee(1,"Vijay Shinde","Male","CNS","Programming")
    e.showEmployee()
    print("\nDoctor Object")
    d = Doctor()
    d.setEmployee(1, "vijay", "male", "aiims", "eyes")
    d.showEmployee()

if __name__=="__main__":
    main()

# Hybrid Inheritance:
# Hybrid Inheritance is the combinations of simple, multiple, multilevel and
# hierarchical inheritance.

# Ex.1
class vehicle:

    def __init__(self, model, mileage, price):
        self.price = price
        self.mileage = mileage
        self.model = model

    def show_details(self):
        print(f'Model : {self.model}')
        print(f'Price : {self.price}')
        print(f'Mileage : {self.mileage}')


class bike(vehicle):

    # Inherit Properties and Override
    def __init__(self, model, mileage, price, tyre, cc):
        super().__init__(model, mileage, price)
        self.cc = cc
        self.tyre = tyre

    # Inherit Behavior and Override
    def show_details(self):
        super().show_details()
        print(f'CC : {self.cc}')
        print(f'Tyres : {self.tyre}')

    # Method of Derived Class
    def rating(self):
        print('4 star')


class car(bike, vehicle):

    def rating(self):
        print('5 star')


bajaj = bike("Dominar", 40, 145000, 2, 500)
tata = car("Safari", 25, 2500000, 4, 2000)

bajaj.show_details()
tata.show_details()

bajaj.rating()
tata.rating()

# Ex.2
class University:
  def __init__(self):
    print("Constructor of the Base class")
    # Initializing a class variable named univ to store university name:
    self.univ = "MIT"
  def display(self):
    print(f"The University name is: {self.univ}")

