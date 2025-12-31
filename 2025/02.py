##### PART 1 #####
def invalid(id: int) -> bool:
    id_str = str(id)
    size = len(id_str) // 2
    if size == 0: 
        return False
    if id_str[:size] == id_str[size:]:
        return True
    else:
        return False
        
def invalid_ids(r: tuple[int, int]) -> list[int]:
    ids = []
    min, max = r
    for i in range(min, max+1):
        if invalid(i):
            ids.append(i)
    return ids

def parse(input: str) -> list[tuple[int, int]]:
    input = input.replace(' ', '').replace('\n', '')
    output = input.split(',')
    for i in range(len(output)):
        output[i] = tuple(int(x) for x in output[i].split('-'))
    return output

with open('02.txt', 'r') as f:
    input = f.read()

ids = []
for r in parse(input):
    ids += [x for x in invalid_ids(r) if x not in ids ]

print(sum(ids))

##### PART 2 (incomplete) #####

def invalid_2(id: int) -> bool:
    id_str = str(id)
    size = len(id_str)
    for i in range(0, size+1):
        pass
    if size == 0: 
        return False
    if id_str[:size] == id_str[size:]:
        return True
    else:
        return False
        
def invalid_ids_2(r: tuple[int, int]) -> list[int]:
    ids = []
    min, max = r
    for i in range(min, max+1):
        if invalid_2(i):
            ids.append(i)
    return ids
