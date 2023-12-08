from .polyomino import Polyomino, Angle

class PShapePolyomino(Polyomino):
    def generate_coordinates(self, position):
        x, y = position
        size_x, size_y = self.size
        coordinates = set()

        if self.rotation in [Angle.A_0, Angle.A_180]:
            # Левая "каемка"
            for i in range(size_x):
                coordinates.add((x, y + i))

            # Правая "каемка"
            for i in range(size_x):
                coordinates.add((x + size_y - 1, y + i))

            # Верхняя часть "каемки"
            if self.rotation == Angle.A_0:
                for i in range(size_y):
                    coordinates.add((x + i, y))
            else:
                for i in range(size_y):
                    coordinates.add((x + i, y + size_x - 1))
        else:
            # Верхняя "каемка"
            for i in range(size_x):
                coordinates.add((x + i, y))

            # Нижняя "каемка"
            for i in range(size_x):
                coordinates.add((x + i, y + size_y - 1))

            # Боковая часть "каемки"
            if self.rotation == Angle.A_90:
                for i in range(size_y):
                    coordinates.add((x, y + i))
            else:
                for i in range(size_y):
                    coordinates.add((x + size_x - 1, y + i))
        
        return coordinates