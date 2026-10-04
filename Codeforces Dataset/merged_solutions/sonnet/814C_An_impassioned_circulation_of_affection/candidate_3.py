import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, str]]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    s = fields[1].decode()
    q = int(fields[2])
    asked = []
    for i in range(q):
        asked.append((int(fields[3 + 2 * i]), fields[4 + 2 * i].decode()))
    return s, asked


# --- clause: best_runs :: (s: str) -> list[list[int]] ---
def best_runs(s):
    n = len(s)
    tables = []
    for letter in range(26):
        ch = chr(97 + letter)
        finest = [0] * (n + 1)
        for begin in range(n):
            cost = 0
            for right in range(begin, n):
                if s[right] != ch:
                    cost += 1
                if cost <= n and right - begin + 1 > finest[cost]:
                    finest[cost] = right - begin + 1
        for budget in range(1, n + 1):
            if finest[budget - 1] > finest[budget]:
                finest[budget] = finest[budget - 1]
        tables.append(finest)
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
