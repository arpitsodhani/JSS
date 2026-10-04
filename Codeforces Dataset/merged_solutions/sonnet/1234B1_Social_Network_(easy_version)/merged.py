import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    k = data[1]
    return k, data[2:2 + n]

# Clause run_screen [Confidence: 0.80]
def run_screen(k, ids):
    shown = []
    for element in ids:
        if element in shown:
            continue
        shown.insert(0, element)
        if len(shown) > k:
            shown.pop()
    return shown

# Clause main [Confidence: 1.00]
def main():
    k, ids = read_input()
    shown = run_screen(k, ids)
    sys.stdout.write("%d\n%s\n" % (len(shown), " ".join(map(str, shown))))


if __name__ == "__main__":
    main()

