##### PART 1 #####
def parse(input: str) -> list[list[int]]:
    input = input.strip('\n').splitlines()
    return [[int(c) for c in line] for line in input]

def largest_joltage(bank: list[int]) -> int:
    digit1 = max(bank[:len(bank)-1])
    digit2 = max(bank[bank.index(digit1)+1:])
    return (digit1 * 10) + digit2

with open('03.txt', 'r') as f:
    input = f.read()

# input = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """
banks = parse(input)

print(sum([largest_joltage(bank) for bank in banks]))

##### PART 2 #####
def largest_joltage_2(bank: list[int]) -> int:
    multipliers = [10**i for i in range(11,-1, -1)]
    digits = []
    prev = -1
    for digit in range(12):
        selection = bank[prev+1:len(bank)-12+digit+1]
        max_selection = max(selection)
        digits.append(max_selection)
        prev += 1+selection.index(max_selection)
    
    value = 0
    for i in range(12):
        value += multipliers[i] * digits[i]
    return value

print(sum([largest_joltage_2(bank) for bank in banks]))
