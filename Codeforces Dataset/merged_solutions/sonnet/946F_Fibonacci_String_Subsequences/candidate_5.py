import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x = int(data[1])
    s = bytes(data[2])
    return n, x, s


# --- clause: base_matrix :: (n: int, s: bytes, letter: int) -> list[list[int]] ---
def base_matrix(n, s, letter):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        if 0 < a < n:
            table[a][a] = 1
        else:
            table[a][a] = 2
        if a < n and letter == s[a]:
            table[a][a + 1] = 1
    return table


# --- clause: multiply :: (n: int, left: list[list[int]], right: list[list[int]]) -> list[list[int]] ---
def multiply(n, left, right):
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        row = left[a]
        dest = out[a]
        b = a
        while b <= n:
            value = row[b]
            if value:
                other = right[b]
                for c in range(b, n + 1):
                    if other[c]:
                        dest[c] = (dest[c] + value * other[c]) % MOD
            b += 1
    return out


# --- clause: count_subsequences :: (n: int, x: int, s: bytes) -> int ---
def count_subsequences(n, x, s):
    older = base_matrix(n, s, 48)
    newer = base_matrix(n, s, 49)
    if x == 0:
        return older[0][n] % MOD
    for _ in range(2, x + 1):
        product = multiply(n, newer, older)
        older = newer
        newer = product
    return newer[0][n] % MOD


# --- clause: main :: () -> None ---
def main():
    n, x, s = read_input()
    sys.stdout.write(str(count_subsequences(n, x, s)) + "\n")


if __name__ == "__main__":
    main()
