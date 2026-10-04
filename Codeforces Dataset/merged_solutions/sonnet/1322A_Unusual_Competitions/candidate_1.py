import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[1].decode()


# --- clause: repair_cost :: (row: str) -> int ---
def repair_cost(row):
    balance = 0
    start = -1
    total = 0
    for i in range(len(row)):
        balance += 1 if row[i] == "(" else -1
        if balance < 0 and start < 0:
            start = i
        if balance == 0 and start >= 0:
            total += i - start + 1
            start = -1
    if balance != 0:
        return -1
    return total


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % repair_cost(read_input()))


if __name__ == "__main__":
    main()
