import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    notes = []
    for token in data[1:n + 1]:
        notes.append(int(token))
    return n, notes


# --- clause: count_rooms :: (n: int, notes: list[int]) -> int ---
def count_rooms(n, notes):
    free = [False] * (n + 2)
    free[0] = True
    rooms = 1
    minute = 1
    while minute <= n:
        note = notes[minute - 1]
        if free[note]:
            free[note] = False
        else:
            rooms += 1
        free[minute] = True
        minute += 1
    return rooms


# --- clause: main :: () -> None ---
def main():
    n, notes = read_input()
    print(count_rooms(n, notes))


if __name__ == "__main__":
    main()
