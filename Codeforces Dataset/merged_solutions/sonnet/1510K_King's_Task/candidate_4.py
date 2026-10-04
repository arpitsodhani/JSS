import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + 2 * n]

# --- clause: apply_op :: (n: int, perm: list[int], kind: int) -> list[int] ---
def apply_op(n, perm, kind):
    result = list(perm)
    if kind == 0:
        for i in range(n):
            result[2 * i], result[2 * i + 1] = perm[2 * i + 1], perm[2 * i]
    else:
        for i in range(n):
            result[i] = perm[n + i]
            result[n + i] = perm[i]
    return result

# --- clause: min_operations :: (n: int, perm: list[int]) -> int ---
def min_operations(n, perm):
    target = list(range(1, 2 * n + 1))
    limit = 4 * n + 5
    best = -1
    for first in (0, 1):
        current = list(perm)
        kind = first
        steps = 0
        while steps <= limit:
            if current == target:
                if best < 0 or steps < best:
                    best = steps
                break
            current = apply_op(n, current, kind)
            kind = 1 - kind
            steps += 1
    return best

# --- clause: main :: () -> None ---
def main():
    n, perm = read_input()
    sys.stdout.write(str(min_operations(n, perm)) + "\n")


if __name__ == "__main__":
    main()
