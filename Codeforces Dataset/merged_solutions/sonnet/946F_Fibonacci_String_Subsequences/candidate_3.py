import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x = int(data[1])
    s = data[2][:n]
    return n, x, s


# --- clause: base_matrix :: (n: int, s: bytes, letter: int) -> list[list[int]] ---
def base_matrix(n, s, letter):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 2
    table[n][n] = 2
    for a in range(1, n):
        table[a][a] = 1
    for a in range(n):
        if s[a] == letter:
            table[a][a + 1] = 1
    return table


# --- clause: multiply :: (n: int, left: list[list[int]], right: list[list[int]]) -> list[list[int]] ---
def multiply(n, left, right):
    out = []
    for a in range(n + 1):
        dest = [0] * (n + 1)
        row = left[a]
        for b in range(a, n + 1):
            value = row[b]
            if value:
                other = right[b]
                for c in range(b, n + 1):
                    dest[c] = (dest[c] + value * other[c]) % MOD
        out.append(dest)
    return out


# --- clause: count_subsequences :: (n: int, x: int, s: bytes) -> int ---
def count_subsequences(n, x, s):
    older = base_matrix(n, s, 48)
    newer = base_matrix(n, s, 49)
    if x == 0:
        return older[0][n] % MOD
    step = 2
    while step <= x:
        older, newer = newer, multiply(n, newer, older)
        step += 1
    return newer[0][n] % MOD


# --- clause: main :: () -> None ---
def main():
    n, x, s = read_input()
    print(count_subsequences(n, x, s))


if __name__ == "__main__":
    main()
