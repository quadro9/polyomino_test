class Table:
    def __init__(self, width, height):
        self.width = width  # Ширина стола
        self.height = height  # Высота стола
        self.grid = [[0] * width for _ in range(height)]  # Инициализация сетки стола

    def display(self):
        # Метод для вывода текущего состояния стола, например, в виде текстовой графики
        for row in self.grid:
            print(" ".join(map(str, row)))
    
    def place_polyomino(self, polyomino, position):
        # Метод для размещения полиомино на столе в указанной позиции
        coordinates = polyomino.generate_coordinates(position)
        
        # Проверка на возможность размещения полиомино на столе
        if self.is_valid_placement(coordinates):
            for x, y in coordinates:
                self.grid[y][x] = polyomino.display
            return True
        else:
            return False

    def is_valid_placement(self, coordinates):
        # Метод для проверки, может ли полиомино быть размещено на столе в указанных координатах
        for x, y in coordinates:
            if not (0 <= x < self.width and 0 <= y < self.height):
                return False  # Проверка выхода за границы стола
            if self.grid[y][x] != 0:
                return False  # Проверка пересечения с другим полиомино
        return True
    
    def remove_polyomino(self, polyomino):
        # Метод для удаления полиомино
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == polyomino.display:
                    self.grid[y][x] = 0

    def clear(self):
        # Метод для очистки всего стола
        for x in range(self.width):
            for y in range(self.height):
                self.grid[y][x] = 0
