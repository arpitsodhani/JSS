import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    n = int(fields[0])
    people = []
    for i in range(n):
        people.append((fields[1 + 2 * i].decode(), int(fields[2 + 2 * i])))
    return people


# --- clause: build_queue :: (people: list[tuple[str, int]]) -> list[tuple[str, int]] | None ---
def build_queue(people):
    n = len(people)
    arranged = sorted(range(n), key=lambda i: people[i][1])
    line = []
    height = n
    for i in arranged:
        name, ahead = people[i]
        if ahead > len(line):
            return None
        line.insert(ahead, (name, height))
        height -= 1
    return line


# --- clause: main :: () -> None ---
def main():
    line = build_queue(read_input())
    if line is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join("%s %d" % entry_row for entry_row in line) + "\n")


if __name__ == "__main__":
    main()
