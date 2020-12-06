def decoder(code, num_rows, num_cols):
    # Row decoder
    start, stop = 0, num_rows - 1
    for i, ch in enumerate(code[:7]):
        if ch == 'F' and i != 6:
            stop = ((stop - start) // 2) + start
        elif ch == 'F' and i == 6:
            row = start
        elif ch == 'B' and i != 6:
            start = ((stop - start) // 2) + start + 1
        else:
            row = stop

    # Column decoder
    start, stop = 0, num_cols - 1
    for i, ch in enumerate(code[7:]):
        if ch == 'L' and i != 2:
            stop = ((stop - start) // 2) + start
        elif ch == 'L' and i == 2:
            col = start
        elif ch == 'R' and i != 2:
            start = ((stop - start) // 2) + start + 1
        else:
            col = stop
    return (row*8) + col

with open('./input.txt', 'r') as f:
    codes = f.read().strip().split()

max_seat_id = 0 
seat_ids = []
for code in codes:
    seat_id = decoder(code, 128, 8)
    seat_ids.append(seat_id)
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)

seat_ids = sorted(seat_ids)

for i, id in enumerate(seat_ids):
    if i == 0:
        continue
    if i == len(seat_ids) - 1:
        continue

    if int(seat_ids[i+1]) == int(id) + 2:
        print(int(id) + 1)
