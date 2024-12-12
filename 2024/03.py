import re

with open('03.txt', 'r') as f:
    content = f.read().strip()

# had to brush up on regexps a bit to solve this - haven't used them in a while 

##### PART 1 #####
instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", content)

total = 0

for inst in instructions:
    num1, num2 = map(int, inst.replace('mul(', '').replace(')', '').strip().split(','))
    total +=  num1 * num2
    
print(total)

##### PART 2 #####
instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", content)

total = 0
enabled = True

for inst in instructions:
    if inst == "do()":
        enabled = True
    elif inst == "don't()":
        enabled = False
    elif enabled:
        num1, num2 = map(int, inst.replace('mul(', '').replace(')', '').strip().split(','))
        total +=  num1 * num2
    
print(total)