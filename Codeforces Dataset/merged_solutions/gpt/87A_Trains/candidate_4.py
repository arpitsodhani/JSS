# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import math

    data = sys.stdin.read().split()
    a, b = map(int, data[:2])

    l = a * b // math.gcd(a, b)
    i = j = 1
    prev = 0
    dasha = 0
    masha = 0

    while i * a <= l or j * b <= l:
        nd = i * a
        nm = j * b

        if nd < nm:
            dasha += nd - prev
            prev = nd
            i += 1
        elif nm < nd:
            masha += nm - prev
            prev = nm
            j += 1
        else:
            if a > b:
                dasha += nd - prev
            elif b > a:
                masha += nd - prev
            prev = nd
            i += 1
            j += 1

    if dasha > masha:
        print("Dasha")
    elif masha > dasha:
        print("Masha")
    else:
        print("Equal")

# CLAUSE: finish_program
def main():
    _inner_main()

main()
