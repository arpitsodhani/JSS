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


# --- clause: jump_cost :: (a: list[int]) -> int ---
def jump_cost(a):
    n = len(a)
    left = 0
    for i in range(n):
        if a[i] == 0:
            break
        left = i
    right = n - 1
    for i in range(n - 1, -1, -1):
        if a[i] == 0:
            break
        right = i
    return 0 if left >= right else right - left


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(jump_cost(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
