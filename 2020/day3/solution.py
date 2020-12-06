# Day 3 Part 1
hill = []
with open('./input_3.txt', 'r') as f:
    for line in f:
        slope = line.strip()
        hill.append(slope)

def count_trees(hill):
    count = 0
    for i in range(len(hill)):
        if i == 0:
            x = y = 0
        else:
            x = i
            y = (x * 3) % (len(hill[0]))
        if hill[x][y] == '#':
            count += 1
    return count

#print(count_trees(hill))

# Day 3 Part 2
def count_trees_many_slopes(hill):
    counts = []
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for right, down in slopes:
        count = 0
        for i in range(0, len(hill), down):
            if right != 1:
                x = i
                y = (x * right) % len(hill[0])
            else:
                x = i
                y = (x // down) % len(hill[0])
            if hill[x][y] == '#':
                count += 1
        counts.append(count)
    return counts

counts = count_trees_many_slopes(hill)
print(counts)
prod = 1
for c in counts:
    prod *= c
print(prod)
