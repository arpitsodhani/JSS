import sys

# Clause read_input [Confidence: 0.60]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rules = []
    for i in range(n):
        rules.append((data[1 + 3 * i].decode(), int(data[2 + 3 * i]), data[3 + 3 * i].decode()))
    return rules

# Clause narrow [Confidence: 0.80]
def narrow(rules):
    low = -2000000000
    high = 2000000000
    for sign, x, answer in rules:
        yes = answer == "Y"
        if sign == ">":
            if yes:
                if x + 1 > low:
                    low = x + 1
            elif x < high:
                high = x
        elif sign == "<":
            if yes:
                if x - 1 < high:
                    high = x - 1
            elif x > low:
                low = x
        elif sign == ">=":
            if yes:
                if x > low:
                    low = x
            elif x - 1 < high:
                high = x - 1
        else:
            if yes:
                if x < high:
                    high = x
            elif x + 1 > low:
                low = x + 1
    if low > high:
        return "Impossible"
    return str(low)

# Clause main [Confidence: 0.40]
def main():
    sys.stdout.write(narrow(read_input()) + "\n")


if __name__ == "__main__":
    main()

