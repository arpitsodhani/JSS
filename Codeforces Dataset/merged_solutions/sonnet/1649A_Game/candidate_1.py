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
    while left + 1 < n and a[left + 1] == 1:
        left += 1
    right = n - 1
    while right - 1 >= 0 and a[right - 1] == 1:
        right -= 1
    if left >= right:
        return 0
    return right - left


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(jump_cost(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
