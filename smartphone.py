   # Assignment 1: Design Your Own Class! 
#    Question 1--------NB:Each of the question is encap with is own comment
# class smartphone:
#      #    Attributes (properties)
#    def __init__(self, make, model, color):
#           self.make = make
#           self.model = model
#           self.color = color

#         # Method (behavior)
#    def start(self):
#         return f"The {self.color} {self.make} {self.model} starts."

#    def stop(self):
#         return f"The {self.color} {self.make} {self.model} stops."
    
    
    
           # Quesion 2
           # ENHANCEMENT AND ADDITTIONAL FEATURES
# class smartphone:
#    def __init__(self, make, model, color, battery):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.battery = battery  # New attribute

#    def start(self):
#         return f"The {self.color} {self.make} {self.model} starts."

#    def stop(self):
#         return f"The {self.color} {self.make} {self.model} stops."

#    def check_battery(self):
#         return f"The battery is at {self.battery}%."
    
#           # simulate a call function
#    def make_call(self, number):
#         return f"Calling {number} from the {self.make} {self.model}."

        # Override the __str__ Method
  
  
  
    # Question 3
class smartphone:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        return f"The {self.color} {self.make} {self.model} starts."

    def stop(self):
        return f"The {self.color} {self.make} {self.model} stops."


class SmartphoneWithFeatures(smartphone):
    def __init__(self, make, model, color, battery, camera_megapixels):
        super().__init__(make, model, color)
        self.__battery = battery  # Private attribute for encapsulation
        self.camera_megapixels = camera_megapixels

    # Polymorphism: Override the start method
    def start(self):
        return f"The advanced {self.color} {self.make} {self.model} is now powered on with {self.__battery}% battery."

    def take_photo(self):
        return f"The {self.make} {self.model} takes a photo with its {self.camera_megapixels}MP camera."

    # Encapsulation: Getter for battery
    def get_battery(self):
        return self.__battery

    # Encapsulation: Setter for battery
    def set_battery(self, new_battery):
        if 0 <= new_battery <= 100:
            self.__battery = new_battery
        else:
            raise ValueError("Battery percentage must be between 0 and 100.")

