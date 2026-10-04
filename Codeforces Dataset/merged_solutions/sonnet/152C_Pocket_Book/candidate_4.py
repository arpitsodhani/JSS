import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    names = [bytes(data[2 + i]) for i in range(n)]
    return n, m, names


# --- clause: count_names :: (n: int, m: int, names: list[bytes]) -> int ---
def count_names(n, m, names):
    total = 1
    for col in range(m):
        seen = set()
        for row in names:
            seen.add(row[col])
        total = total * len(seen) % MOD
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, names = read_input()
    answer = count_names(n, m, names)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
