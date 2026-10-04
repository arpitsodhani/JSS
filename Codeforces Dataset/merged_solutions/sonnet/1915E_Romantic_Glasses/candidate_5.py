import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: has_balanced :: (a: list[int]) -> bool ---
def has_balanced(a):
    seen = {0}
    running = 0
    even = True
    for value in a:
        running = running + value if even else running - value
        even = not even
        if running in seen:
            return True
        seen.add(running)
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if has_balanced(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
