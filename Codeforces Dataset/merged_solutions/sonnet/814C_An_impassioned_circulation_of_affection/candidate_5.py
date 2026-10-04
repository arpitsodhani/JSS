import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, str]]] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    s = raw[1].decode()
    q = int(raw[2])
    asked = []
    for i in range(q):
        asked.append((int(raw[3 + 2 * i]), raw[4 + 2 * i].decode()))
    return s, asked


# --- clause: best_runs :: (s: str) -> list[list[int]] ---
def best_runs(s):
    n = len(s)
    tables = []
    for letter in range(26):
        ch = chr(97 + letter)
        top = [0] * (n + 1)
        for first_side in range(n):
            cost = 0
            for right in range(first_side, n):
                if s[right] != ch:
                    cost += 1
                if cost <= n and right - first_side + 1 > top[cost]:
                    top[cost] = right - first_side + 1
        for budget in range(1, n + 1):
            if top[budget - 1] > top[budget]:
                top[budget] = top[budget - 1]
        tables.append(top)
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
