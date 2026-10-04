import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode(), raw[2].decode()


# --- clause: pair_cost :: (x: str, y: str, p: str, q: str) -> int ---
def pair_cost(x, y, p, q):
    if p == q:
        return 0 if x == y else 1
    matched = 0
    pool = [p, q]
    for ch in (x, y):
        if ch in pool:
            pool.remove(ch)
            matched += 1
    return 2 - matched


# --- clause: preprocess_moves :: (a: str, b: str) -> int ---
def preprocess_moves(a, b):
    n = len(a)
    running = 0
    for i in range(n // 2):
        j = n - 1 - i
        running += pair_cost(a[i], a[j], b[i], b[j])
    if n % 2 and a[n // 2] != b[n // 2]:
        running += 1
    return running


# --- clause: main :: () -> None ---
def main():
    a, b = read_input()
    sys.stdout.write("%d\n" % preprocess_moves(a, b))


if __name__ == "__main__":
    main()
