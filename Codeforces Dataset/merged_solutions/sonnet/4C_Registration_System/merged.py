import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]

# Clause register_all [Confidence: 1.00]
def register_all(names):
    seen = {}
    out = []
    for name in names:
        if name in seen:
            count = seen[name]
            seen[name] = count + 1
            out.append(name + str(count))
        else:
            seen[name] = 1
            out.append("OK")
    return out

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("\n".join(register_all(read_input())) + "\n")


if __name__ == "__main__":
    main()

