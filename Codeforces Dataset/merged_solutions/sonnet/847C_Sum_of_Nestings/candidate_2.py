import sys


# --- clause: read_input :: () -> tuple[int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1]


# --- clause: build_sequence :: (n: int, k: int) -> str | None ---
def build_sequence(n, k):
    if k > n * (n - 1) // 2:
        return None
    deep = 0
    while (deep + 1) * deep // 2 <= k and deep < n:
        deep += 1
    if deep * (deep - 1) // 2 > k:
        deep -= 1
    rest = k - deep * (deep - 1) // 2
    pieces = ["(" * deep]
    low = n - deep
    if low > 0:
        pieces.append(")" * (deep - rest))
        pieces.append("(")
        pieces.append(")" * (rest + 1))
        low -= 1
        pieces.append("()" * low)
    else:
        pieces.append(")" * deep)
    return "".join(pieces)


# --- clause: main :: () -> None ---
def main():
    n, k = read_input()
    answer = build_sequence(n, k)
    sys.stdout.write("Impossible\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()
