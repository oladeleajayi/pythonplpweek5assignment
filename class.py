# from smartphone import smartphone

# smartphone1 = smartphone("Samsung", "Galaxy S23", "white,")
# smartphone2 = smartphone("Techno", "Camon5", "blue")


# Importing the smartphone class
from smartphone import smartphone

# Creating objects (instances of the smartphone class)
smartphone1 = smartphone("Samsung", "Galaxy S23", "white", 85)
smartphone2 = smartphone("Techno", "Camon5", "blue", 70)

# Interacting with the objects
print(smartphone1.start())  # Output: The white Samsung Galaxy S23 starts.
print(smartphone1.stop())   # Output: The white Samsung Galaxy S23 stops.

print(smartphone2.start())  # Output: The blue Techno Camon5 starts.
print(smartphone2.stop())   # Output: The blue Techno Camon5 stops.


 # Enhancement and addittional features
  # Creating the smartphone1 object
smartphone1 = smartphone("Samsung", "Galaxy S23", "white", 85)

 # Creating smartphone2 object 
smartphone2 = smartphone("Techno", "Camon 5", "blue", 70)

 # Calling methods on the object
print(smartphone1.start())         # Output: The white Samsung Galaxy S23 starts.
print(smartphone1.check_battery()) # Output: The battery is at 85%.

print(smartphone2.start())         # Output: The blue Techno Camon5 starts.
print(smartphone2.check_battery()) # Output: The battery is at 70%.

 # Simulate a call function
print(smartphone1.make_call("+1234567890"))  
 # Output: Calling +1234567890 from the Samsung Galaxy S23


 # Override the __str__ Method
print(smartphone1)  
 # Output: White Samsung Galaxy S23
