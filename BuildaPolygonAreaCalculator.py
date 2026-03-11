class Rectangle():
    def __init__(self,width,height):
        self.width = width 
        self.height = height 

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ("*" * self.width + "\n") * self.height
            return picture
    
    def get_amount_inside(self, shape):
        h = self.width // shape.width
        v = self.height // shape.height
        return h * v

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, value):
        self.width = value
        self.height = value

    def set_height(self, value):
        self.width = value
        self.height = value

    def set_side(self, value):
        self.set_width(value)

    def __str__(self):
        return f"Square(side={self.height})"