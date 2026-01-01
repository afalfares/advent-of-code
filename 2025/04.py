##### PART 1 #####
from itertools import product

def parse(input: str) -> list[list[str]]:
    input = input.strip("\n").strip().splitlines()
    return [[col for col in row] for row in input]

def accessible(
    grid: list[list[str]],
    cord_x: int, 
    cord_y: int
) -> bool:
    relative_pos = product([-1, 0, 1], [-1, 0, 1])

    adjacents = [(cord_x + a, cord_y + b) for a,b in relative_pos if not (a == 0 and b == 0)]

    count = 0 
    for x, y in adjacents:
        if x < 0 or y < 0:
            continue
        try:
            if grid[y][x] in ['@', 'X']:
                count += 1
                if count >= 4:
                    return False
        except IndexError:
            continue
    return True

def accessible_count(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    out_grid = grid.copy()
    count = 0
    for y in range(len(out_grid)):
        for x in range(len(out_grid[y])):
            if out_grid[y][x] == '@' and accessible(out_grid, x, y):
                out_grid[y][x] = 'X'
                count += 1
    return count, out_grid

with open('04.txt', 'r') as f:
    input = f.read()

grid = parse(input)
count, _ = accessible_count(grid)        
print(count)

##### PART 2 #####
def remove_x(grid: list[list[str]]) -> tuple[bool, list[list[str]]]:
    has = False
    out_grid = grid.copy()
    
    for y in range(len(out_grid)):
        for x in range(len(out_grid[y])):
            if out_grid[y][x] == "X":
                out_grid[y][x] = "."
                has = True
    return has, out_grid

def accessible_count_2(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    out_grid = grid.copy()
    count = 0
    while True:
        c, out_grid = accessible_count(out_grid)
        count += c
        cont, out_grid = remove_x(out_grid)
        
        if not cont: 
            break

    return count, out_grid

grid = parse(input)
count, grid = accessible_count_2(grid)
print(count)


