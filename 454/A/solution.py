def solve():
    n = int(input())
    score = n // 2
    lst = []
    for i in range(score, -1, -1):
        string = "*" * i + "D" * (n - 2*i) + "*" * i
        lst.append(string)

    for j in lst:
        print(j)
    for index, k in enumerate(lst[::-1]):
        if index == 0:
            continue
        print(k)

solve()
