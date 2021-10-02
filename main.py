import math


class Circle(object):
    def __init__(self, r=1.0, precision=2):
        self.pi = float("{0:.{1}f}".format(math.pi, precision))
        self.precision = precision
        self.r = r
    
    def circumference(self):
        formula = 2 * self.pi * self.r
        return float("{0:.{1}f}".format(formula, self.precision))

    def area(self):
        formula = 2 * self.pi * math.pow(self.r, 2)
        return float("{0:.{1}f}".format(formula, self.precision))

    def __str__(self):
        return f"Circumference is: {self.circumference()}", f"Area is: {self.area()}"


for i in range(54):
    print(i, "=>", Circle(r=1, precision=i).__str__())
