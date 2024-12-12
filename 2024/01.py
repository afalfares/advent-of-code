arr1 = []
arr2 = []

with open('01.txt', 'r') as f:
    for line in f.read().strip().splitlines():
        col1, col2 = map(int, line.split("   "))
        arr1.append(col1)
        arr2.append(col2)

arr1.sort()
arr2.sort()

assert len(arr2) == len(arr1)

tot_dist = 0
sim = 0
for i in range(len(arr1)):
    tot_dist += abs(arr1[i] - arr2[i])
    sim += arr1[i] * arr2.count(arr1[i])

print(tot_dist) # part 1
print(sim) # part 2
    
    