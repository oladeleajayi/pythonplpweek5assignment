# Question 1-----NB:Each of the question is encap with is own comment
from smartphone import smartphone

# smartphone1 = smartphone("Samsung", "Galaxy S23", "white,")
# smartphone2 = smartphone("Techno", "Camon5", "blue")



# Question 2
# # Importing the smartphone class
# from smartphone import smartphone

# # Creating objects (instances of the smartphone class)
# smartphone1 = smartphone("Samsung", "Galaxy S23", "white", 85)
# smartphone2 = smartphone("Techno", "Camon5", "blue", 70)

# # Interacting with the objects
# print(smartphone1from smartphone import smartphone.start())  # Output: The white Samsung Galaxy S23 starts.
# print(smartphone1.stop())   # Output: The white Samsung Galaxy S23 stops.

# print(smartphone2.start())  # Output: The blue Techno Camon5 starts.
# print(smartphone2.stop())   # Output: The blue Techno Camon5 stops.


#  # Enhancement and addittional features
#   # Creating the smartphone1 object
# smartphone1 = smartphone("Samsung", "Galaxy S23", "white", 85)

#  # Creating smartphone2 object 
# smartphone2 = smartphone("Techno", "Camon 5", "blue", 70)

#  # Calling methods on the object
# print(smartphone1.start())         # Output: The white Samsung Galaxy S23 starts.
# print(smartphone1.check_battery()) # Output: The battery is at 85%.

# print(smartphone2.start())         # Output: The blue Techno Camon5 starts.
# print(smartphone2.check_battery()) # Output: The battery is at 70%.

#  # Simulate a call function
# print(smartphone1.make_call("+1234567890"))  
#  # Output: Calling +1234567890 from the Samsung Galaxy S23


#  # Override the __str__ Method
# print(smartphone1)  
#  # Output: White Samsung Galaxy S23




# Question 3
# Demonstrating Inheritance, Polymorphism, and Encapsulation
# Base class object
from smartphone import smartphone

basic_phone = smartphone("Nokia", "3310", "blue")
print(basic_phone.start())  # Output: The blue Nokia 3310 starts.

# Subclass object
from smartphone import SmartphoneWithFeatures
advanced_phone = SmartphoneWithFeatures("Apple", "iPhone 14 Pro", "black", 85, 48)
print(advanced_phone.start())  # Polymorphism in action
# Output: The advanced black Apple iPhone 14 Pro is now powered on with 85% battery.

print(advanced_phone.take_photo())  
# Output: The Apple iPhone 14 Pro takes a photo with its 48MP camera.

# Encapsulation in Action
# Access the private battery attribute via getter
print(advanced_phone.get_battery())  # Output: 85

# Modify the private battery attribute via setter
advanced_phone.set_battery(95)
print(advanced_phone.get_battery())  # Output: 95

# Attempting to set an invalid battery value
try:
    advanced_phone.set_battery(120)  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Battery percentage must be between 0 and 100.
