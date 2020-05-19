'''
Python Solution to Codeforces Contest 520 Problem B
Author: Jordan Ung <jordanung@protonmail.com>
Last Modified: <20.05.20>

Solution Methodology: This solution is built on the principle that given an
integer n, 2n - 2 can be achieved in 2 steps: n -> n-1 -> 2(n-1) rather than
n -> 2n -> 2n-1 -> 2n-2 (3 steps). For that reason, there should be at most
1 blue button press (subtraction) after a red button press (multiplication).
By moving the subtractions before a multiplication, we can remove half of the
blue button presses with each consecutive move.

e.g. 6 -> 12(*) -> 11(-) -> 10(-) can be done with 6 -> 5(-) -> 10(*)
'''
import math
def solve():
    n, m = list(map(int, input().split(" ")))

    # Exclusively pressing blue button i.e. -1 until m is reached
    if m <= n:
        print(n - m)
        return
    
    # How how many times n needs to be multiplied to be greater than m
    multiplier = int(math.ceil(math.log2(m / n)))
    
    # Represents amount of -1's needed after consecutively multiplying by 2
    count = 2 ** multiplier * n - m

    total = multiplier

    for i in range(multiplier):
        if count <= 1:
            break
        elif count % 2 == 1:
            total += 1

        count = count // 2
    print(total + count)

solve()
