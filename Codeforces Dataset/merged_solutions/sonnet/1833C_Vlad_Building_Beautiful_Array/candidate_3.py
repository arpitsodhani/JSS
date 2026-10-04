import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: can_build :: (a: list[int]) -> bool ---
def can_build(a):
    least_odd = -1
    least_even = -1
    for element in a:
        if element % 2:
            if least_odd < 0 or element < least_odd:
                least_odd = element
        else:
            if least_even < 0 or element < least_even:
                least_even = element
    if least_odd < 0 or least_even < 0:
        return True
    return least_odd < least_even


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if can_build(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
