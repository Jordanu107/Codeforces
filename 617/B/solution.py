def solve():
    numbers = int(input())
    lst = [int(x) for x in input().split(" ")]
    add = sum
    if add(lst) <= 1:
        print(add(lst))
        return
    elif add(lst) == len(lst):
        print(1)
        return

    left_index = lst.index(1) # First occurence of a nut
    right_index = left_index

    for i in range(left_index, len(lst)):
        if lst[i] == 1:
            right_index = i
            break
    
    total = 1
    while right_index < len(lst):
        if lst[right_index] == 1:
            delta = right_index - left_index
            total *= max(1, delta)
            left_index = right_index
        right_index += 1
    print(total)
solve()
