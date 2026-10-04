import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    cases = []
    pos = 1
    for _ in range(t):
        pos += 1
        cases.append(data[pos].decode())
        pos += 1
    return cases

# --- clause: total_imbalance :: (s: str) -> int ---
def total_imbalance(s):
    n = len(s)
    counts = [0] * (2 * n + 1)
    balance = n
    counts[balance] = 1
    for ch in s:
        if ch == "1":
            balance += 1
        else:
            balance -= 1
        counts[balance] += 1
    total = 0
    seen = 0
    running = 0
    for value in range(2 * n + 1):
        c = counts[value]
        if c:
            total += c * (value * seen - running)
            seen += c
            running += c * value
    return total

# --- clause: solve_case :: (s: str) -> int ---
def solve_case(s):
    n = len(s)
    lengths = n * (n + 1) * (n + 2) // 6
    return (lengths + total_imbalance(s)) // 2

# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(solve_case(s)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
