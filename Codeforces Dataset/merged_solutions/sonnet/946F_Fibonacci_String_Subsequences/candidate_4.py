import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x = int(data[1])
    s = data[2]
    return n, x, s


# --- clause: base_matrix :: (n: int, s: bytes, letter: int) -> list[list[int]] ---
def base_matrix(n, s, letter):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        free = 2 if (a == 0 or a == n) else 1
        table[a][a] = free
        if a != n and s[a] == letter:
            table[a][a + 1] = 1
    return table


# --- clause: multiply :: (n: int, left: list[list[int]], right: list[list[int]]) -> list[list[int]] ---
def multiply(n, left, right):
    out = [[0] * (n + 1) for _ in range(n + 1)]
    for a in range(n + 1):
        dest = out[a]
        for c in range(a, n + 1):
            acc = 0
            for b in range(a, c + 1):
                value = left[a][b]
                if value:
                    acc += value * right[b][c]
            dest[c] = acc % MOD
    return out


# --- clause: count_subsequences :: (n: int, x: int, s: bytes) -> int ---
def count_subsequences(n, x, s):
    zero = base_matrix(n, s, 48)
    one = base_matrix(n, s, 49)
    if x == 0:
        return zero[0][n] % MOD
    if x == 1:
        return one[0][n] % MOD
    older = zero
    newer = one
    for _ in range(x - 1):
        product = multiply(n, newer, older)
        older = newer
        newer = product
    return newer[0][n] % MOD


# --- clause: main :: () -> None ---
def main():
    n, x, s = read_input()
    answer = count_subsequences(n, x, s)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
