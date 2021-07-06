from math import sqrt, pow

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x + b.x, a.y + b.y)
        return Vector2(a.x + b, a.y + b)

    def __sub__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x - b.x, a.y - b.y)
        return Vector2(a.x - b, a.y - b)

    def __mul__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x * b.x, a.y * b.y)
        return Vector2(a.x * b, a.y * b)

    def __truediv__(a, b):
        if type(b) == Vector2:
            return Vector2(a.x / b.x, a.y / b.y)
        return Vector2(a.x / b, a.y / b)

    def magnitude(self):
        return sqrt(pow(self.x,2) + pow(self.y,2))

    def normalize(self):
        mg = self.mag()
        if mg == 0:
            self.x = 0
            self.y = 0
        self.x /= mg
        self.y /= mg

    def setMagnitude(self, newMagnitude):
        return Normalize(self) * newMagnitude

    def ParseToInt(self):
        return (int(self.x), int(self.y))

    def __repr__(self):
        return f"vec2({self.x}, {self.y})\n"

def GetMagnitude(a):
    return sqrt(pow(a.x,2) + pow(a.y,2))

def Normalize(a):
    mg = GetMagnitude(a)
    if mg == 0:
        return Vector2()
    return Vector2(a.x/mg, a.y/mg)

def SetMagnitude(vec, mag):
    normalizedVec = Normalize(vec)
    return normalizedVec * mag

def GetDistance2D(a, b):
    difference = b - a
    return difference.magnitude()

#
# b = Vector2(3, 0)
# print(b.setMagnitude(12))
