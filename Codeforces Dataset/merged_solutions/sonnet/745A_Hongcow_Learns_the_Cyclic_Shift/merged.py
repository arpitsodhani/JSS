import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()

# Clause count_shifts [Confidence: 0.80]
def count_shifts(s):
    marked = set()
    entry_row = s
    for _ in range(len(s)):
        entry_row = entry_row[-1] + entry_row[:-1]
        marked.add(entry_row)
    return len(marked)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % count_shifts(read_input()))


if __name__ == "__main__":
    main()

