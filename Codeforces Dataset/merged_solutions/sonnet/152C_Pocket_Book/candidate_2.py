import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    names = list(data[2:2 + n])
    return n, m, names


# --- clause: count_names :: (n: int, m: int, names: list[bytes]) -> int ---
def count_names(n, m, names):
    total = 1
    for col in range(m):
        seen = {row[col] for row in names}
        total = total * len(seen) % MOD
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, names = read_input()
    sys.stdout.write("%d\n" % count_names(n, m, names))


if __name__ == "__main__":
    main()
