import sys

MOD = 1000000007


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    names = [data[2 + i] for i in range(n)]
    return n, m, names


# --- clause: count_names :: (n: int, m: int, names: list[bytes]) -> int ---
def count_names(n, m, names):
    total = 1
    for col in range(m):
        distinct = 0
        table = [0] * 26
        for row in names:
            k = row[col] - 65
            if table[k] == 0:
                table[k] = 1
                distinct += 1
        total = total * distinct % MOD
    return total


# --- clause: main :: () -> None ---
def main():
    n, m, names = read_input()
    sys.stdout.write(str(count_names(n, m, names)) + "\n")


if __name__ == "__main__":
    main()
