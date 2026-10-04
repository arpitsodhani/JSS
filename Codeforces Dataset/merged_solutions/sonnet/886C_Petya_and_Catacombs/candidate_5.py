import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    notes = list(map(int, data[1:1 + n]))
    return n, notes


# --- clause: count_rooms :: (n: int, notes: list[int]) -> int ---
def count_rooms(n, notes):
    free = [False] * (n + 2)
    free[0] = True
    rooms = 1
    for minute in range(1, n + 1):
        note = notes[minute - 1]
        reused = free[note]
        if reused:
            free[note] = False
        else:
            rooms += 1
        free[minute] = True
    return rooms


# --- clause: main :: () -> None ---
def main():
    n, notes = read_input()
    sys.stdout.write(str(count_rooms(n, notes)) + "\n")


if __name__ == "__main__":
    main()
