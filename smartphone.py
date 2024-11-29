# Assignment 1: Design Your Own Class! 
class smartphone:
    # Attributes (properties)
    # def __init__(self, make, model, color):
    #     self.make = make
    #     self.model = model
    #     self.color = color

    # # Method (behavior)
    # def start(self):
    #     return f"The {self.color} {self.make} {self.model} starts."

    # def stop(self):
    #     return f"The {self.color} {self.make} {self.model} stops."
    
         # ENHANCEMENT AND ADDITTIONAL FEATURES
class smartphone:
    def __init__(self, make, model, color, battery):
        self.make = make
        self.model = model
        self.color = color
        self.battery = battery  # New attribute

    def start(self):
        return f"The {self.color} {self.make} {self.model} starts."

    def stop(self):
        return f"The {self.color} {self.make} {self.model} stops."

    def check_battery(self):
        return f"The battery is at {self.battery}%."
    
          # simulate a call function
    def make_call(self, number):
        return f"Calling {number} from the {self.make} {self.model}."

        # Override the __str__ Method
    def __str__(self):
        return f"{self.color.capitalize()} {self.make} {self.model}"
