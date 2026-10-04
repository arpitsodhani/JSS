import sys


# --- clause: read_input :: () -> tuple[int, list[str], str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    x = int(data[2])
    rows = [data[3 + i].decode() for i in range(n)]
    return x, rows, data[4 + n].decode()


# --- clause: reachable_letters :: (x: int, rows: list[str]) -> set[str] ---
def reachable_letters(x, rows):
    n = len(rows)
    m = len(rows[0])
    shifts = []
    for i in range(n):
        for j in range(m):
            if rows[i][j] == "S":
                shifts.append((i, j))
    easy = set()
    for i in range(n):
        for j in range(m):
            ch = rows[i][j]
            if ch == "S":
                continue
            for si, sj in shifts:
                if (si - i) * (si - i) + (sj - j) * (sj - j) <= x * x:
                    easy.add(ch)
                    break
    return easy


# --- clause: count_helps :: (rows: list[str], easy: set[str], text: str) -> int ---
def count_helps(rows, easy, text):
    plain = set()
    shifts = 0
    for row in rows:
        for ch in row:
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
