import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()

# Clause transform [Confidence: 0.60]
def transform(text):
    vowels = "aoyeui"
    out = []
    for ch in text.lower():
        if ch in vowels:
            continue
        out.append(".")
        out.append(ch)
    return "".join(out)

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write(transform(read_input()) + "\n")


if __name__ == "__main__":
    main()

