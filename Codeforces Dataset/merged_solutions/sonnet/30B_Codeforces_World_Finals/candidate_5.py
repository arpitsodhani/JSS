import sys


# --- clause: read_input :: () -> tuple[tuple[int, int, int], tuple[int, int, int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    head = data[0].split(b".")
    tail = data[1].split(b".")
    finals = (int(head[0]), int(head[1]), int(head[2]))
    birth = (int(tail[0]), int(tail[1]), int(tail[2]))
    return finals, birth


# --- clause: valid_date :: (day: int, month: int, year: int) -> bool ---
def valid_date(day, month, year):
    if year < 1 or year > 99:
        return False
    if month < 1 or month > 12:
        return False
    lengths = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    limit = lengths[month - 1]
    if year % 4 == 0 and month == 2:
        limit = 29
    return 1 <= day <= limit


# --- clause: can_take_part :: (finals: tuple[int, int, int], birth: tuple[int, int, int]) -> str ---
def can_take_part(finals, birth):
    day, month, year = finals
    a, b, c = birth
    orders = ((a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a))
    for bd, bm, by in orders:
        if not valid_date(bd, bm, by):
            continue
        if (by + 18, bm, bd) <= (year, month, day):
            return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    finals, birth = read_input()
    answer = can_take_part(finals, birth)
    sys.stdout.write(answer + "\n")


if __name__ == "__main__":
    main()
