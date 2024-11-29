class car:
    def move(self):
        return "driving!"

class Plane:
    def move(self):
        return "flying!"


# Polymorphism in action
for vehicle in [car(), Plane()]:
    try:
        print(vehicle.move())
    except AttributeError as e:
        print("Ooops, we have an error", e)