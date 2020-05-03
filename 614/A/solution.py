def solve():
    l, r, k = list(map(int, input().split(" ")))
    lst = []
    count = 0
    while k ** count <= r:
        if k ** count >= l:
            lst.append(k ** count)
        count += 1
    if len(lst) == 0:
        print(-1)
    else:
        print(" ".join([str(x) for x in lst]))

solve()
