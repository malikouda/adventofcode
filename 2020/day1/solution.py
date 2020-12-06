def find_two(nodes, target):
    for n1 in nodes:
        for n2 in nodes:
            if n1 + n2 == target: return n1*n2

with open('./input_1.txt', 'r') as f:
    nodes = f.read().strip().split('\n')

nodes = list(map(int, nodes))

print(find_two(nodes, 2020))

def find_three(nodes, target):
    for n1 in nodes:
        if n1 >= target: continue
        for n2 in nodes:
            if n1 + n2 >= target: continue
            for n3 in nodes:
                if n1 + n2 + n3 == target: return n1*n2*n3
    return None

print(find_three(nodes, 2020))
