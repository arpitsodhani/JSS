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


# --- clause: count_segments :: (a: list[int]) -> int ---
def count_segments(a):
    n = len(a)
    required = set()
    seen = set()
    missing = 0
    pieces = 0
    for value in a:
        if value not in seen:
            seen.add(value)
            if value in required:
                missing -= 1
        if missing == 0:
            pieces += 1
            for item in seen:
                required.add(item)
            seen = set()
            missing = len(required)
    return pieces


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_segments(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
