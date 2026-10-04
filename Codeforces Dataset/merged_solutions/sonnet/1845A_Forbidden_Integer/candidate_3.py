import sys


# --- clause: read_input :: () -> list[tuple[int, int, int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cases = []
    for i in range(t):
        cases.append((fields[1 + 3 * i], fields[2 + 3 * i], fields[3 + 3 * i]))
    return cases


# --- clause: build_sum :: (n: int, k: int, x: int) -> list[int] | None ---
def build_sum(n, k, x):
    if x != 1:
        return [1] * n
    if k < 2:
        return None
    if n % 2 == 0:
        return [2] * (n // 2)
    if k < 3:
        return None
    return [3] + [2] * ((n - 3) // 2)


# --- clause: main :: () -> None ---
def main():
    collected = []
    for n, k, x in read_input():
        parts = build_sum(n, k, x)
        if parts is None:
            collected.append("NO")
        else:
            collected.append("YES")
            collected.append(str(len(parts)))
            collected.append(" ".join(map(str, parts)))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
