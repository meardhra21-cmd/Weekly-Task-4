class Rectangle:
    
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def update_dimensions(self, new_length, new_breadth):
        if new_length > 0 and new_breadth > 0:
            self.length = new_length
            self.breadth = new_breadth
            print("Dimensions updated successfully!")
        else:
            print("Length and breadth must be positive values.")


rect1 = Rectangle(10, 5)

print("Initial Area:", rect1.calculate_area())

rect1.update_dimensions(20, 10)

print("Updated Area:", rect1.calculate_area())
