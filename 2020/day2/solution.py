passwords = []
with open('./input_2.txt', 'r') as f:
    for line in f:
        password = line.strip().split()
        password[0] = list(map(int, password[0].split('-')))
        password[1] = password[1][0]
        passwords.append(password)

def is_valid(start, stop, letter, word):
    count = 0
    for ch in word:
        if ch == letter: count += 1
        if count > stop: return False
    if count < start: return False
    return True

def count_valid(nodes):
    count = 0
    for node in nodes:
        bounds, letter, password = node 
        start, stop = bounds
        if is_valid(start, stop, letter, password): count += 1
    return count

print(count_valid(passwords))

def is_valid_position(i, j, letter, word):
    count = 0    
    for k in [i, j]:
        if k > 0 and k <= len(word) + 1:
            if word[k - 1] == letter:
                count += 1
    return count == 1

def count_valid_position(nodes):
    count = 0
    for node in nodes:
        idxs, letter, password = node
        i, j = idxs
        if is_valid_position(i, j, letter, password): count += 1
    return count

print(count_valid_position(passwords))
