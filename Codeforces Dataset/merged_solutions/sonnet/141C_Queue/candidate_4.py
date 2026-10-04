import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    n = int(numbers[0])
    people = []
    for i in range(n):
        people.append((numbers[1 + 2 * i].decode(), int(numbers[2 + 2 * i])))
    return people


# --- clause: build_queue :: (people: list[tuple[str, int]]) -> list[tuple[str, int]] | None ---
def build_queue(people):
    n = len(people)
    order = sorted(range(n), key=lambda i: -people[i][1])
    slots = [None] * n
    height = 1
    for i in order:
        name, ahead = people[i]
        seat = -1
        free = 0
        for spot in range(n):
            if slots[spot] is not None:
                continue
            if free == ahead:
                seat = spot
                break
            free += 1
        if seat < 0:
            return None
        slots[seat] = (name, height)
        height += 1
    return slots


# --- clause: main :: () -> None ---
def main():
    line = build_queue(read_input())
    if line is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join("%s %d" % row for row in line) + "\n")


if __name__ == "__main__":
    main()
