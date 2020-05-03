count, bounds = [int(x) for x in input().split(" ")]
lst = [int(x) for x in input().split(" ")]
lst.sort()


right_index = count - 1
left_index = 0
highest = 0
current_num = -1

# Find left most index where number is greater than or equal to bounds
for index, i in enumerate(lst):
    if i < bounds:
        left_index += 1
        continue
    break

while right_index >= left_index:
    # Same number as before, no need to check
    if lst[left_index] == current_num:
        left_index += 1
        continue

    # Different Number
    current_num = lst[left_index]

    for j in range(current_num, bounds-1, -1):
        current = 0
        for i in range(left_index, right_index + 1):
            # Add maximum possible
            current += (lst[i] // j) * j
        # print("L:", left_index, "| R:", right_index, "current:", current)
        if current > highest:
            highest = current
    left_index += 1

print(highest)
