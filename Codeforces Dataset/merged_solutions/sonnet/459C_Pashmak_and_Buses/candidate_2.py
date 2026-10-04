import sys


# --- clause: read_input :: () -> tuple[int, int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[0], tokens[1], tokens[2]


# --- clause: enough_room :: (n: int, k: int, d: int) -> bool ---
def enough_room(n, k, d):
    room = 1
    for _ in range(d):
        room *= k
        if room >= n:
            return True
    return room >= n


# --- clause: seat_plan :: (n: int, k: int, d: int) -> list[list[int]] ---
def seat_plan(n, k, d):
    rows = [[0] * n for _ in range(d)]
    for student in range(n):
        item = student
        for day in range(d):
            rows[day][student] = item % k + 1
            item //= k
    return rows


# --- clause: main :: () -> None ---
def main():
    n, k, d = read_input()
    if not enough_room(n, k, d):
        sys.stdout.write("-1\n")
        return
    out = []
    for row in seat_plan(n, k, d):
        out.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
