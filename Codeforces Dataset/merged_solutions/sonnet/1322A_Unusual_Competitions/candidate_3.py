import sys


# --- clause: read_input :: () -> str ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[1].decode()


# --- clause: repair_cost :: (row: str) -> int ---
def repair_cost(row):
    balance = 0
    from_here = -1
    tally = 0
    for i in range(len(row)):
        balance += 1 if row[i] == "(" else -1
        if balance < 0 and from_here < 0:
            from_here = i
        if balance == 0 and from_here >= 0:
            tally += i - from_here + 1
            from_here = -1
    if balance != 0:
        return -1
    return tally


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % repair_cost(read_input()))


if __name__ == "__main__":
    main()
