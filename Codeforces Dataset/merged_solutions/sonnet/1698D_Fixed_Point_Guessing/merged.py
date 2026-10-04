import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    line = sys.stdin.readline()
    while line.strip() == "":
        line = sys.stdin.readline()
    return int(line)

# Clause ask [Confidence: 1.00]
def ask(l, r):
    sys.stdout.write("? " + str(l) + " " + str(r) + "\n")
    sys.stdout.flush()
    values = []
    while len(values) < r - l + 1:
        line = sys.stdin.readline()
        if not line:
            break
        for token in line.split():
            values.append(int(token))
    return values

# Clause find_fixed [Confidence: 1.00]
def find_fixed(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high) // 2
        values = ask(low, mid)
        inside = 0
        for value in values:
            if low <= value <= mid:
                inside += 1
        if inside % 2 == 1:
            high = mid
        else:
            low = mid + 1
    return low

# Clause main [Confidence: 1.00]
def main():
    for _ in range(read_input()):
        n = read_input()
        answer = find_fixed(n)
        sys.stdout.write("! " + str(answer) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()

