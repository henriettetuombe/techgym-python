# Define the Smartphone class
class Smartphone:
    def __init__(self, type, size, color):
        self.type = type  # Smartphone type (e.g., Android or iPhone)
        self.size = size  # Screen size
        self.color = color  # Smartphone color

    def info(self):
        # Print smartphone information
        print(f"type:{self.type} size:{self.size} color:{self.color}")


# Data for smartphones (type, size, color)
data = [
    ("Android", 60, "red"),
    ("iPhone", 50, "blue"),
    ("Android", 70, "white"),
    ("Android", 50, "black"),
    ("Android", 60, "purple"),
    ("iPhone", 60, "black"),
    ("Android", 50, "green"),
    ("iPhone", 70, "yellow"),
    ("iPhone", 80, "purple"),
    ("Android", 60, "yellow"),
]

# Create an array to store Smartphone instances
Smartphones = []

# Create instances using a for loop and add them to the array
for item in data:
    phone = Smartphone(item[0], item[1], item[2])
    Smartphones.append(phone)

# Display the information of all smartphones
for phone in Smartphones:
    phone.info()