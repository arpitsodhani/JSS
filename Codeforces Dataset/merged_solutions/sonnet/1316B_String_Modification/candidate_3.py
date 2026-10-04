import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        s = data[pos + 1].decode()
        pos += 2
        cases.append((n, s))
    return cases


# --- clause: shifted :: (n: int, s: str, k: int) -> str ---
def shifted(n, s, k):
    head = s[k - 1:]
    tail = s[:k - 1]
    if (n - k) % 2 == 0:
        tail = tail[::-1]
    return head + tail


# --- clause: best_choice :: (n: int, s: str) -> tuple[str, int] ---
def best_choice(n, s):
    best = shifted(n, s, 1)
    pick = 1
    for k in range(2, n + 1):
        candidate = shifted(n, s, k)
        if candidate < best:
            best = candidate
            pick = k
    return best, pick


# --- clause: main :: () -> None ---
def main():
    out = []
    for n, s in read_input():
        text, k = best_choice(n, s)
        out.append(text)
        out.append(str(k))
    print("\n".join(out))


if __name__ == "__main__":
    main()
