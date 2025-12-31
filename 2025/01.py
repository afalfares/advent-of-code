"""
Though process:
start 50 

0 -> 99, loops around
"""
##### PART 1 #####
def rotate(current: int, direction: str, amount: int) -> int:
    
    if direction == "L":
        return (current - amount) % 100
    else:
        return (current + amount) % 100

def crack_password(rotations: list[str]) -> None:
    password = 0
    dial_pos = 50
    
    for rotation in rotations:
        if rotation.strip() == "":
            continue
        direction = rotation[:1]
        amount = int(rotation[1:])
        dial_pos = rotate(dial_pos, direction, amount)
        if dial_pos == 0:
            password += 1

    print(f"Password: {password}")

with open('01.txt', 'r') as f:
    rotations = f.readlines()

crack_password(rotations)

##### PART 2 (incomplete) #####

test = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]
 
def count_zero_crossing(current: int, direction: str, amount:int) -> int:
    crossings = 0
    if direction == "L":
        if amount >= 100:
            crossings = amount // 100
            remainder = amount % 100
            if current < remainder:
                crossings += 1 
        else:
            if current < amount:
                crossings = 1
    else:
        if amount >= 100:
            crossings = amount // 100
            remainder = amount % 100
            if current + remainder >= 100:
                crossings += 1
        else:
            if current + amount >= 100:
                crossings = 1

    return crossings

def crack_password_2(rotations: list[str]):
    password = 0
    dial_pos = 50
    
    for rotation in rotations:
        if rotation.strip() == "":
            continue
        direction = rotation[:1]
        amount = int(rotation[1:])
        password += count_zero_crossing(dial_pos, direction, amount)
        dial_pos = rotate(dial_pos, direction, amount)
        

    print(f"Password: {password}")

crack_password_2(test)