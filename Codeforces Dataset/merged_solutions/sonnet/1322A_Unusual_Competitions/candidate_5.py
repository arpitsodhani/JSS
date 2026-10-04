import sys


# --- clause: read_input :: () -> str ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[1].decode()


# --- clause: repair_cost :: (row: str) -> int ---
def repair_cost(row):
    balance = 0
    begin = -1
    running = 0
    for i in range(0, len(row)):
        balance += 1 if row[i] == "(" else -1
        if balance < 0 and begin < 0:
            begin = i
        if balance == 0 and begin >= 0:
            running += i - begin + 1
            begin = -1
    if balance != 0:
        return -1
    return running


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % repair_cost(read_input()))


if __name__ == "__main__":
    main()
