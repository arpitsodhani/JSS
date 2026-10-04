import sys


# --- clause: read_input :: () -> tuple[int, list[str], str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    x = int(numbers[2])
    rows = [numbers[3 + i].decode() for i in range(n)]
    return x, rows, numbers[4 + n].decode()


# --- clause: reachable_letters :: (x: int, rows: list[str]) -> set[str] ---
def reachable_letters(x, rows):
    n = len(rows)
    m = len(rows[0])
    easy = set()
    for i in range(n):
        for j in range(m):
            if rows[i][j] != "S":
                continue
            low = i - x if i - x > 0 else 0
            high = i + x + 1 if i + x + 1 < n else n
            for y in range(low, high):
                for z in range(m):
                    ch = rows[y][z]
                    if ch == "S":
                        continue
                    if (y - i) * (y - i) + (z - j) * (z - j) <= x * x:
                        easy.add(ch)
    return easy


# --- clause: count_helps :: (rows: list[str], easy: set[str], text: str) -> int ---
def count_helps(rows, easy, text):
    plain = set()
    shifts = 0
    for record in rows:
        for ch in record:
            if ch == "S":
                shifts += 1
            else:
                plain.add(ch)
    helps = 0
    for ch in text:
        if ch.islower():
            if ch not in plain:
                return -1
        else:
            small = ch.lower()
            if small not in plain or shifts == 0:
                return -1
            if small not in easy:
                helps += 1
    return helps


# --- clause: main :: () -> None ---
def main():
    x, rows, text = read_input()
    easy = reachable_letters(x, rows)
    sys.stdout.write("%d\n" % count_helps(rows, easy, text))


if __name__ == "__main__":
    main()
