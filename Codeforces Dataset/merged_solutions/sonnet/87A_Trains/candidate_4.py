import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[0], numbers[1]


# --- clause: gcd_of :: (a: int, b: int) -> int ---
def gcd_of(a, b):
    while b:
        a, b = b, a % b
    return a


# --- clause: who_wins :: (a: int, b: int) -> str ---
def who_wins(a, b):
    period = a // gcd_of(a, b) * b
    marks = []
    step = a
    while step <= period:
        marks.append((step, 0))
        step += a
    step = b
    while step <= period:
        marks.append((step, 1))
        step += b
    marks.sort()
    dasha = 0
    masha = 0
    here = 0
    i = 0
    while i < len(marks):
        moment, kind = marks[i]
        if i + 1 < len(marks) and marks[i + 1][0] == moment:
            if a > b:
                dasha += moment - here
            else:
                masha += moment - here
            i += 2
        else:
            if kind == 0:
                dasha += moment - here
            else:
                masha += moment - here
            i += 1
        here = moment
    if dasha > masha:
        return "Dasha"
    return "Masha" if masha > dasha else "Equal"


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write(who_wins(a, b) + "\n")


if __name__ == "__main__":
    main()
