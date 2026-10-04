import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    lines = sys.stdin.read().split("\n")
    count = int(lines[0])
    return [line.rstrip("\r") for line in lines[1:1 + count]]

# Clause whose_line [Confidence: 0.40]
def whose_line(line):
    score = 0
    if line.endswith("lala."):
        score += 1
    if line.startswith("miao."):
        score += 2
    if score == 1:
        return "Freda's"
    if score == 2:
        return "Rainbow's"
    return "OMG>.< I don't know!"

# Clause main [Confidence: 1.00]
def main():
    out = []
    for line in read_input():
        out.append(whose_line(line))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

