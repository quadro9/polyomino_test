from enum import Enum

class Angle(Enum):
    A_0 = 0
    A_90 = 1
    A_180 = 2
    A_270 = 3

class Polyomino:
    def __init__(self, size, display):
        self.size = size
        self.display = display
        self.rotation = Angle.A_0
    
    def rotate(self, angle):
        if angle not in Angle:
            raise ValueError("Недопустимый угол")
        self.rotation = angle

    def __str__(self):
        return f"Размер: {self.size}, Отображение: {self.display}"


