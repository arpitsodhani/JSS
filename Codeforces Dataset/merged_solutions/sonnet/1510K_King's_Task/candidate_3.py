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
    target = tuple(range(1, 2 * n + 1))
    start = tuple(perm)
    seen = {start: 0}
    queue = [start]
    head = 0
    while head < len(queue):
        state = queue[head]
        head += 1
        if state == target:
            return seen[state]
        for kind in (0, 1):
            nxt = tuple(apply_op(n, list(state), kind))
            if nxt not in seen:
                seen[nxt] = seen[state] + 1
                queue.append(nxt)
    return -1

# --- clause: main :: () -> None ---
def main():
    n, perm = read_input()
    sys.stdout.write(str(min_operations(n, perm)) + "\n")


if __name__ == "__main__":
    main()
