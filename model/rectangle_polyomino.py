from .polyomino import Angle, Polyomino


class RectanglePolyomino(Polyomino):
    def generate_coordinates(self, position):
        x, y = position
        size_x, size_y = self.size
        if self.rotation in [Angle.A_90, Angle.A_270]:
            size_x, size_y = size_y, size_x
        coordinates = set()

        for i in range(size_x):
            for j in range(size_y):
                point = (x + i, y + j)
                coordinates.add(point)
        
        return coordinates