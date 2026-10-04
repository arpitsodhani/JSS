import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: can_build :: (a: list[int]) -> bool ---
def can_build(a):
    least_odd = -1
    least_even = -1
    for item in a:
        if item % 2:
            if least_odd < 0 or item < least_odd:
                least_odd = item
        else:
            if least_even < 0 or item < least_even:
                least_even = item
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
