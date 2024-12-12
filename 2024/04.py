with open('04.txt', 'r') as f:
    grid = [[c for c in line.strip()] for line in f.read().strip().splitlines()]
    rows = len(grid)
    cols = len(grid[0])

##### PART 1 #####
KEYWORD = 'XMAS'
DIRECTIONS = (
    (0, 1),
    (1, 0), 
    (0, -1), 
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
)

def search(start_r, start_c, direction):
    dr, dc = direction 
    for i in range(len(KEYWORD)):
        r2 = start_r + i * dr
        c2 = start_c + i * dc
        if (
            not (0 <= r2 < rows and 0 <= c2 < cols) or 
            grid[r2][c2] != KEYWORD[i]
        ):
            return False
    return True

count = 0 

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == KEYWORD[0]:
            for d in DIRECTIONS:
                if search(r, c, d): count += 1

print(count)

##### PART 2 #####
XKEYWORD = 'MAS'
XDIRECTIONS = (
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
)
XING_START_DIRECTIONS = (
    (0, 1),
    (1, 0), 
    (0, -1), 
    (-1, 0)
)

center_coords = []

def searchX(start_r, start_c, direction):
    dr, dc = direction 
    
    center = 1
    center_coord = None
    
    for i in range(len(XKEYWORD)):
        r2 = start_r + i * dr
        c2 = start_c + i * dc
        if (
            not (0 <= r2 < rows and 0 <= c2 < cols) or 
            grid[r2][c2] != XKEYWORD[i]
        ):
            return False
        
        if i == center:
            center_coord = (r2, c2)
    
    assert center_coord is not None
    
    if center_coord not in center_coords: # avoid repeating Xs
        # look for any XING MAS's
        for s_r, s_c in ((start_r + 2 * d1, start_c + 2 * d2) for d1, d2 in XING_START_DIRECTIONS):
            for d in XDIRECTIONS:
                if searchX2(s_r, s_c, d, center_coord):
                    center_coords.append(center_coord)
                    return True
    return False

def searchX2(start_r, start_c, direction, center_coord):
    dr, dc = direction 
    
    center = 1
    
    for i in range(len(XKEYWORD)):
        r2 = start_r + i * dr
        c2 = start_c + i * dc
        if (
            not (0 <= r2 < rows and 0 <= c2 < cols) or 
            grid[r2][c2] != XKEYWORD[i] or 
            ( # ensure the center is matching (i.e, they cross)
                i == center and 
                (r2, c2) != center_coord
            )
        ):
            return False
    return True

count = 0 

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == XKEYWORD[0]:
            for d in XDIRECTIONS:
                if searchX(r, c, d): count += 1

print(count)