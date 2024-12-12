with open('05.txt', 'r') as f:
    rules_str, updates_str = f.read().strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_str.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_str.splitlines()]

##### PART 1 #####
def valid(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

sum = 0 
for update in updates:
    if valid(update):
        sum += update[len(update)//2]
print(sum)

##### PART 2 #####
        