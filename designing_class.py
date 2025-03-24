# this is work  submision on class and all is described below 

class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery  # Encapsulated (private) attribute

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.model} charged to {self.__battery}% battery.")

    def get_battery(self):  # Encapsulation - controlled access
        return self.__battery

# Inheritance: AdvancedPhone extends Smartphone
class AdvancedPhone(Smartphone):
    def __init__(self, brand, model, battery, camera_quality):
        super().__init__(brand, model, battery)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"{self.model} takes a {self.camera_quality}MP photo!")

# Creating objects
phone1 = AdvancedPhone("Apple", "iPhone 15", 80, 48)
phone1.charge(10)
print(phone1.get_battery())
phone1.take_photo()


