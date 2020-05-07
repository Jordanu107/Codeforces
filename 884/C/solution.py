#### Solution: C. Bertown Subway
#### <https://codeforces.com/contest/884/problem/C>
#### Author: Jordan Ung <jordanung@protonmail.com>
#### Last Updated: 07.05.20

def solve():
    stations = int(input())
    arr = [int(x) - 1 for x in input().split(" ")]
    cycles = []
 
    discovered = {}
    for i in arr:
        # Already part of a cycle found
        if i in discovered:
            continue
        
        count = 1
        dest = arr[i]
        path = [dest]
        discovered[dest] = 1

        # While still have nodes that are reachable
        while dest != i:
            count += 1
            dest = arr[dest]
            path.append(dest)
            discovered[dest] = 1
 
        cycles.append(path)
 
    # The whole graph is one cycle
    if len(cycles) == 1:
        print(stations * stations)
        return
 
    # Join the two largest cycles
    longest = sorted(cycles, key=len)[len(cycles) - 2:]
    joined = longest[0] + longest[1]
    cycles = sorted(cycles, key=len)[:len(cycles) - 2]
    cycles.append(joined)
 
    # Find total amount of combinations
    total = 0
    for cycle in cycles:
        total += len(cycle) ** 2
    print(total)
solve()
