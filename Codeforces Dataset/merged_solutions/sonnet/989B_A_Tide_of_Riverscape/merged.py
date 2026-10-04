import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return int(data[1]), data[2].decode()

# Clause break_period [Confidence: 1.00]
def break_period(p, s):
    band = list(s)
    n = len(band)
    for i in range(n - p):
        a = band[i]
        b = band[i + p]
        if a != "." and b != "." and a != b:
            broken = True
        elif a == "." and b == ".":
            band[i] = "0"
            band[i + p] = "1"
        elif a == ".":
            band[i] = "1" if b == "0" else "0"
        elif b == ".":
            band[i + p] = "1" if a == "0" else "0"
        else:
            continue
        for j in range(n):
            if band[j] == ".":
                band[j] = "0"
        return "".join(band)
    return None

# Clause main [Confidence: 1.00]
def main():
    p, s = read_input()
    answer = break_period(p, s)
    sys.stdout.write("No\n" if answer is None else answer + "\n")


if __name__ == "__main__":
    main()

