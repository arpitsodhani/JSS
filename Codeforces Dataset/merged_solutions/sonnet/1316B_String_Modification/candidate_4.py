import sys


# --- clause: read_input :: () -> list[tuple[int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        s = data[pos].decode()
        pos += 1
        cases.append((n, s))
    return cases


# --- clause: shifted :: (n: int, s: str, k: int) -> str ---
def shifted(n, s, k):
    prefix = s[:k - 1]
    if (n - k) % 2 == 0:
        prefix = "".join(reversed(prefix))
    return s[k - 1:] + prefix


# --- clause: best_choice :: (n: int, s: str) -> tuple[str, int] ---
def best_choice(n, s):
    best = None
    pick = 1
    for k in range(1, n + 1):
        candidate = shifted(n, s, k)
        if best is None or candidate < best:
            best = candidate
            pick = k
    return best, pick


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        text, k = best_choice(case[0], case[1])
        out.append(text)
        out.append(str(k))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
