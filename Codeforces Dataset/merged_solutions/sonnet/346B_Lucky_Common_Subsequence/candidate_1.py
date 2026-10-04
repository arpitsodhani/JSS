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
    width = (n2 + 1) * v
    size = (n1 + 1) * width
    best = [-1] * size
    parent = [-1] * size
    letter = [0] * size
    best[0] = 0
    for i in range(n1 + 1):
        for j in range(n2 + 1):
            base = i * width + j * v
            for k in range(v):
                here = base + k
                score = best[here]
                if score < 0:
                    continue
                if i < n1:
                    nxt = here + width
                    if best[nxt] < score:
                        best[nxt] = score
                        parent[nxt] = here
                        letter[nxt] = 0
                if j < n2:
                    nxt = here + v
                    if best[nxt] < score:
                        best[nxt] = score
                        parent[nxt] = here
                        letter[nxt] = 0
                if i < n1 and j < n2 and s1[i] == s2[j]:
                    state = table[k][ord(s1[i]) - 65]
                    if state < v:
                        nxt = (i + 1) * width + (j + 1) * v + state
                        if best[nxt] < score + 1:
                            best[nxt] = score + 1
                            parent[nxt] = here
                            letter[nxt] = ord(s1[i])
    final = -1
    top = -1
    for k in range(v):
        here = n1 * width + n2 * v + k
        if best[here] > top:
            top = best[here]
            final = here
    if top <= 0:
        return "0"
    chars = []
    while parent[final] >= 0:
        if letter[final]:
            chars.append(chr(letter[final]))
        final = parent[final]
    chars.reverse()
    return "".join(chars)


# --- clause: main :: () -> None ---
def main():
    s1, s2, virus = read_input()
    table = build_automaton(virus)
    sys.stdout.write(longest_clean(s1, s2, virus, table) + "\n")


if __name__ == "__main__":
    main()
