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
    balance = 0
    prefixes = [0] * (len(s) + 1)
    for i, ch in enumerate(s):
        balance = balance + 1 if ch == "1" else balance - 1
        prefixes[i + 1] = balance
    prefixes.sort()
    running = 0
    total = 0
    for rank, value in enumerate(prefixes):
        total += rank * value - running
        running += value
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
