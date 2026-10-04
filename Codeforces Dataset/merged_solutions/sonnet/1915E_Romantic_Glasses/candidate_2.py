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
    prefix = [0] * (len(a) + 1)
    running = 0
    for i, value in enumerate(a):
        running = running + value if i % 2 == 0 else running - value
        prefix[i + 1] = running
    prefix.sort()
    for i in range(len(prefix) - 1):
        if prefix[i] == prefix[i + 1]:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if has_balanced(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
