with open('input.txt', 'r') as f:
    groups = f.read().strip().split('\n\n')

groups = [group.split('\n') for group in groups]

answer_sets = []
count = 0
for group in groups:
    combined = ''
    for person in group:
        combined += person
    count += len(set(combined))

print(count)

count = 0
for group in groups:
    count += len(set.intersection(*[set(a) for a in group]))

print(count)
