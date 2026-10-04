import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[0], data[1]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: who_wins :: (a: int, b: int) -> str ---
def who_wins(a, b):
    period = a // gcd_of(a, b) * b
    dasha = 0
    masha = 0
    here = 0
    step_a = a
    step_b = b
    while here < period:
        if step_a < step_b:
            dasha += step_a - here
            here = step_a
            step_a += a
        elif step_b < step_a:
            masha += step_b - here
            here = step_b
            step_b += b
        else:
            if a > b:
                dasha += step_a - here
            else:
                masha += step_b - here
            here = step_a
            step_a += a
            step_b += b
    if dasha > masha:
        return "Dasha"
    return "Masha" if masha > dasha else "Equal"


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(who_wins(a, b) + "\n")


if __name__ == "__main__":
    main()
