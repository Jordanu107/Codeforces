import math

count, bounds = [int(x) for x in input().split(" ")]
total = 0

left_index = 0
right_index = 2
current = 0

lst = [int(x) for x in input().split(" ")]
if lst[0] < 0:
    delta = 1 - lst[0]
    lst = [x + delta for x in lst]

while right_index < len(lst):
    if lst[right_index] - lst[left_index] <= bounds:
        right_index += 1
        continue
    elements = right_index - left_index - 1
    total += elements * (elements - 1) / 2
    left_index += 1

while left_index < len(lst) - 2:
    if lst[count-1] - lst[left_index] <= bounds:
        elements = count - left_index - 2
        total += elements * (elements + 1) / 2
        left_index += 1
print(int(total))
