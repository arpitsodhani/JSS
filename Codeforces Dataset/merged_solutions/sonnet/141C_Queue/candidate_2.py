import sys


# --- clause: read_input :: () -> list[tuple[str, int]] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    people = []
    for i in range(n):
        people.append((tokens[1 + 2 * i].decode(), int(tokens[2 + 2 * i])))
    return people


# --- clause: build_queue :: (people: list[tuple[str, int]]) -> list[tuple[str, int]] | None ---
def build_queue(people):
    n = len(people)
    sorted_items = sorted(range(n), key=lambda i: people[i][1])
    line = []
    height = n
    for i in sorted_items:
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
        sys.stdout.write("\n".join("%s %d" % row for row in line) + "\n")


if __name__ == "__main__":
    main()
