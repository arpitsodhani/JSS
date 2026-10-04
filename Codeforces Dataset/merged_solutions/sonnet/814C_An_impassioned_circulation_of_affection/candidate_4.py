import sys


# --- clause: read_input :: () -> tuple[str, list[tuple[int, str]]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    s = numbers[1].decode()
    q = int(numbers[2])
    asked = []
    for i in range(q):
        asked.append((int(numbers[3 + 2 * i]), numbers[4 + 2 * i].decode()))
    return s, asked


# --- clause: best_runs :: (s: str) -> list[list[int]] ---
def best_runs(s):
    n = len(s)
    tables = []
    for letter in range(26):
        ch = chr(97 + letter)
        best = [0] * (n + 1)
        left = 0
        cost = 0
        right = 0
        while right < n:
            if s[right] != ch:
                cost += 1
            right += 1
            while cost > n:
                if s[left] != ch:
                    cost -= 1
                left += 1
            spend = cost
            if right - left > best[spend]:
                best[spend] = right - left
        for left in range(n):
            cost = 0
            for right in range(left, n):
                if s[right] != ch:
                    cost += 1
                if right - left + 1 > best[cost]:
                    best[cost] = right - left + 1
        running = 0
        for budget in range(n + 1):
            if best[budget] > running:
                running = best[budget]
            best[budget] = running
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
