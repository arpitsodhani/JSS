import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    return n, data[1:1 + 2 * n]

# --- clause: apply_op :: (n: int, perm: list[int], kind: int) -> list[int] ---
def apply_op(n, perm, kind):
    if kind == 0:
        result = list(perm)
        for i in range(0, 2 * n, 2):
            result[i] = perm[i + 1]
            result[i + 1] = perm[i]
        return result
    return perm[n:] + perm[:n]

# --- clause: min_operations :: (n: int, perm: list[int]) -> int ---
def min_operations(n, perm):
    target = list(range(1, 2 * n + 1))
    limit = 4 * n + 5
    best = -1
    for kind in (0, 1):
        current = list(perm)
        steps = 0
        while steps <= limit:
            if current == target:
                if best < 0 or steps < best:
                    best = steps
                break
            current = apply_op(n, current, kind)
            kind ^= 1
            steps += 1
    return best

# --- clause: main :: () -> None ---
def main():
    n, perm = read_input()
    sys.stdout.write(str(min_operations(n, perm)) + "\n")


if __name__ == "__main__":
    main()
