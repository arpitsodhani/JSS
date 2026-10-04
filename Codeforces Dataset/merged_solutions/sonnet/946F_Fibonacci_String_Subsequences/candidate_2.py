import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, x = int(data[0]), int(data[1])
    return n, x, data[2]


# --- clause: base_matrix :: (n: int, s: bytes, letter: int) -> list[list[int]] ---
def base_matrix(n, s, letter):
    table = []
    for a in range(n + 1):
        row = [0] * (n + 1)
        row[a] = 2 if a in (0, n) else 1
        if a < n and s[a] == letter:
            row[a + 1] = 1
        table.append(row)
    return table


# --- clause: multiply :: (n: int, left: list[list[int]], right: list[list[int]]) -> list[list[int]] ---
def multiply(n, left, right):
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for b in range(n + 1):
        other = right[b]
        for a in range(b + 1):
            value = left[a][b]
            if not value:
                continue
            dest = out[a]
            for c in range(b, n + 1):
                if other[c]:
                    dest[c] = (dest[c] + value * other[c]) % MOD
    return out


# --- clause: count_subsequences :: (n: int, x: int, s: bytes) -> int ---
def count_subsequences(n, x, s):
    blocks = [base_matrix(n, s, 48), base_matrix(n, s, 49)]
    if x <= 1:
        return blocks[x][0][n] % MOD
    for step in range(2, x + 1):
        blocks.append(multiply(n, blocks[step - 1], blocks[step - 2]))
        blocks[step - 2] = None
    return blocks[x][0][n] % MOD


# --- clause: main :: () -> None ---
def main():
    n, x, s = read_input()
    sys.stdout.write("%d\n" % count_subsequences(n, x, s))


if __name__ == "__main__":
    main()
