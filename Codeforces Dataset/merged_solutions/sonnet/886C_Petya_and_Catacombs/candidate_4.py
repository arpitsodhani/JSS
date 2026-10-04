import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    notes = [int(data[i + 1]) for i in range(n)]
    return n, notes


# --- clause: count_rooms :: (n: int, notes: list[int]) -> int ---
def count_rooms(n, notes):
    rooms = 1
    free = [False] * (n + 2)
    free[0] = True
    for minute in range(1, n + 1):
        note = notes[minute - 1]
        if free[note]:
            free[note] = False
        else:
            rooms += 1
        free[minute] = True
    return rooms


# --- clause: main :: () -> None ---
def main():
    n, notes = read_input()
    answer = count_rooms(n, notes)
    sys.stdout.write(str(answer) + "\n")


if __name__ == "__main__":
    main()
