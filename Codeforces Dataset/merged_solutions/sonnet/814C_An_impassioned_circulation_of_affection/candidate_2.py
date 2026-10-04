import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, str]]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    s = tokens[1].decode()
    q = int(tokens[2])
    asked = []
    for i in range(q):
        asked.append((int(tokens[3 + 2 * i]), tokens[4 + 2 * i].decode()))
    return s, asked


# --- clause: best_runs :: (s: str) -> list[list[int]] ---
def best_runs(s):
    n = len(s)
    tables = []
    for letter in range(26):
        ch = chr(97 + letter)
        best = [0] * (n + 1)
        for low in range(n):
            cost = 0
            for right in range(low, n):
                if s[right] != ch:
                    cost += 1
                if cost <= n and right - low + 1 > best[cost]:
                    best[cost] = right - low + 1
        for budget in range(1, n + 1):
            if best[budget - 1] > best[budget]:
                best[budget] = best[budget - 1]
        tables.append(best)
    return tables


# --- clause: main :: () -> None ---
def main():
    s, asked = read_input()
    tables = best_runs(s)
    out = []
    for budget, ch in asked:
        table = tables[ord(ch) - 97]
        spot = budget if budget < len(table) - 1 else len(table) - 1
        out.append(table[spot])
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
