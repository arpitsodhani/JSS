import sys


# --- clause: read_input :: () -> tuple[str, str, str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode(), data[1].decode(), data[2].decode()


# --- clause: build_automaton :: (virus: str) -> list[list[int]] ---
def build_automaton(virus):
    size = len(virus)
    fail = [0] * size
    border = 0
    for i in range(1, size):
        while border and virus[i] != virus[border]:
            border = fail[border - 1]
        if virus[i] == virus[border]:
            border += 1
        fail[i] = border
    table = []
    for state in range(size):
        row = [0] * 26
        for code in range(26):
            letter = chr(65 + code)
            here = state
            while here and virus[here] != letter:
                here = fail[here - 1]
            row[code] = here + 1 if virus[here] == letter else 0
        table.append(row)
    return table


# --- clause: longest_clean :: (s1: str, s2: str, virus: str, table: list[list[int]]) -> str ---
def longest_clean(s1, s2, virus, table):
    n1 = len(s1)
    n2 = len(s2)
    v = len(virus)
    best = [[[-1] * v for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    came = [[[None] * v for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    best[0][0][0] = 0
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            row = best[i][j]
            for k in range(v):
                score = row[k]
                if score < 0:
                    continue
                if i < n1 and best[i + 1][j][k] < score:
                    best[i + 1][j][k] = score
                    came[i + 1][j][k] = (i, j, k, "")
                if j < n2 and best[i][j + 1][k] < score:
                    best[i][j + 1][k] = score
                    came[i][j + 1][k] = (i, j, k, "")
                if i < n1 and j < n2 and s1[i] == s2[j]:
                    state = table[k][ord(s1[i]) - 65]
                    if state < v and best[i + 1][j + 1][state] < score + 1:
                        best[i + 1][j + 1][state] = score + 1
                        came[i + 1][j + 1][state] = (i, j, k, s1[i])
    top = -1
    end = 0
    for k in range(v):
        if best[n1][n2][k] > top:
            top = best[n1][n2][k]
            end = k
    if top <= 0:
        return "0"
    pieces = []
    i, j, k = n1, n2, end
    while came[i][j][k] is not None:
        pi, pj, pk, ch = came[i][j][k]
        if ch:
            pieces.append(ch)
        i, j, k = pi, pj, pk
    pieces.reverse()
    return "".join(pieces)


# --- clause: main :: () -> None ---
def main():
    s1, s2, virus = read_input()
    table = build_automaton(virus)
    sys.stdout.write(longest_clean(s1, s2, virus, table) + "\n")


if __name__ == "__main__":
    main()
