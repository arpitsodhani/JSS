import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    people = []
    for i in range(n):
        people.append((data[1 + 2 * i].decode(), int(data[2 + 2 * i])))
    return people

# Clause build_queue [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
def main():
    line = build_queue(read_input())
    if line is None:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("\n".join("%s %d" % band for band in line) + "\n")


if __name__ == "__main__":
    main()

