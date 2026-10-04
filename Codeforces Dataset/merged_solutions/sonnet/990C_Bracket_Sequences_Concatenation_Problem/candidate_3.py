import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    return [fields[1 + i].decode() for i in range(n)]


# --- clause: tally_shapes :: (rows: list[str]) -> tuple[dict[int, int], dict[int, int]] ---
def tally_shapes(rows):
    opens = {}
    closes = {}
    for entry_row in rows:
        balance = 0
        lowest = 0
        for ch in entry_row:
            balance += 1 if ch == "(" else -1
            if balance < lowest:
                lowest = balance
        if lowest >= 0:
            opens[balance] = opens.get(balance, 0) + 1
        if lowest >= balance:
            closes[-balance] = closes.get(-balance, 0) + 1
    return opens, closes


# --- clause: count_pairs :: (opens: dict[int, int], closes: dict[int, int]) -> int ---
def count_pairs(opens, closes):
    summed = 0
    for value in opens:
        if value in closes:
            summed += opens[value] * closes[value]
    return summed


# --- clause: main :: () -> None ---
def main():
    opens, closes = tally_shapes(read_input())
    sys.stdout.write("%d\n" % count_pairs(opens, closes))


if __name__ == "__main__":
    main()
