def solve():
    nums = int(input())
    numbers = list(map(int, input().split(" ")))


    # Case 1)
    # Sorted = print 0
    if numbers == sorted(numbers):
        print(0)
        return

    # Case 2) Sorted from highest to lowest
    highest_index = numbers.index(max(numbers))
    while highest_index < len(numbers) - 1:
        if numbers[highest_index] == numbers[highest_index + 1]:
            highest_index += 1
        else:
            break

    lst1 = numbers[:highest_index+1]
    lst2 = numbers[highest_index+1:]

    if lst1 == sorted(lst1) and lst2 == sorted(lst2) and lst2[-1] <= lst1[0]:
        print(len(lst2))
    else:
        print(-1)

solve()
