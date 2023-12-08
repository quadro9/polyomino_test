import ast
import sys

from model import Table, RectanglePolyomino, PShapePolyomino
from model import Angle


def parse_input(input_str):
    lines = input_str.strip().split('\n')
    
    parsed_value = ast.literal_eval(lines[0])
    table = Table(parsed_value[0], parsed_value[1])

    display = 1
    polyominoes = []
    parsed_value = ast.literal_eval(lines[1])
    for value in parsed_value:
        count = value[1]
        for _ in range(count):
            polyominoes.append(RectanglePolyomino(value[0], display))
            display += 1

    parsed_value = ast.literal_eval(lines[2])
    for value in parsed_value:
        count = value[1]
        for _ in range(count):
            polyominoes.append(PShapePolyomino(value[0], display))
            display += 1

    return table, polyominoes



# input_data = "(4, 6)\n[((2, 2), 2)]\n[((3, 4), 1), ((2, 3), 1)]"
input_data = ""
for line in sys.stdin:
    input_data += line
table, polyominoes = parse_input(input_data)

def solve(index):
    if index == len(polyominoes):
        return True
    
    polyomino = polyominoes[index]
    for x in range(table.width):
        for y in range(table.height):
            position = (x, y)
            for angle in Angle:
                polyomino.rotate(angle)

                if table.place_polyomino(polyomino, position):
                    if solve(index+1):
                        return True
                    else:
                        table.remove_polyomino(polyomino)
    
    return False
    
    

print(solve(0))
# table.display()
