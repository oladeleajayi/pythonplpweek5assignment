from smartphone import smartphone

smartphone1 = smartphone("Samsung", "Galaxy S23", "white," )
smartphone2 = smartphone("Techno", "Camon5", "blue")


# Interacting with objects
print(smartphone1.start())  # Output: The white Samsung Galaxy starts.
print(smartphone2.stop())   # Output: The blue Techno Camon5 stops.

# Enhancement and addittional features
smartphone1 = smartphone1("Samsung", "Galaxy S23", "white")
# smartphone1= smartphone2("Techno", "Camon5", "blue")

print(smartphone1.start())         # Output: The white Samsung Galaxy S23 starts.
print(smartphone1.check_battery()) # Output: The battery is at 85%.

# simulate a call function
print(smartphone1.make_call("+1234567890"))  
# Output: Calling +1234567890 from the Samsung Galaxy S23.

# Override the __str__ Method
print(smartphone1)  
# Output: White Samsung Galaxy S23
