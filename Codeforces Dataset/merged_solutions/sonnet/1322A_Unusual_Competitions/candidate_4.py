import sys


# --- clause: read_input :: () -> str ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[1].decode()


# --- clause: repair_cost :: (row: str) -> int ---
def repair_cost(row):
    balance = 0
    bad = 0
    inside = False
    for ch in row:
        balance += 1 if ch == "(" else -1
        if inside:
            bad += 1
            if balance == 0:
                inside = False
        elif balance < 0:
            inside = True
            bad += 1
    if balance != 0:
        return -1
    return bad


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % repair_cost(read_input()))


if __name__ == "__main__":
    main()
