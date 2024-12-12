with open('02.txt', 'r') as f:
    reports = [list(map(int, line.split(" "))) for line in f.read().strip().splitlines()]

def safe(report):
    increasing = None
    for l1, l2 in zip(report, report[1:]):
        dist = l1 - l2
        if not 1 <= abs(dist) <= 3:
            return False 
        if increasing is None:
            increasing = True if dist < 0 else False
        elif (
            (dist < 0 and not increasing) or 
            (dist > 0 and increasing)
        ):
            return False
    return True

def safe_dampen(report): # could time complexity be reduced here? I think so but unsure how
    return any(safe(report[:i] + report[i+1:]) for i in range(len(report)))

def assess_report(dampen: bool = False):
    safe_count = 0
    func = safe_dampen if dampen else safe
    for report in reports:
        if func(report):
            safe_count += 1
    print(safe_count)

assess_report(dampen=False) # part 1
assess_report(dampen=True) # part 2
