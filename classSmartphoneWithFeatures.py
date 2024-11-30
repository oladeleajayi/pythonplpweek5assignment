# Question 3
# Demonstrating Inheritance, Polymorphism, and Encapsulation
class SmartphoneWithFeatures(smartphone):
    def __init__(self, make, model, color, battery, camera_megapixels):
        # Call the constructor of the base class
        super().__init__(make, model, color)
        self.__battery = battery  # Private attribute (encapsulation)
        self.camera_megapixels = camera_megapixels  # New public attribute

    # New method
    def take_photo(self):
        return f"The {self.make} {self.model} takes a photo with its {self.camera_megapixels}MP camera."

    # Encapsulation: getter for battery
    def get_battery(self):
        return self.__battery

    # Encapsulation: setter for battery
    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")

    # Polymorphism: override start method
    def start(self):
        return f"The advanced {self.color} {self.make} {self.model} is now powered on with {self.__battery}% battery."
