import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    text = sys.stdin.read()
    if text.endswith("\n"):
        text = text[:-1]
    return [line.rstrip("\r") for line in text.split("\n")]

# Clause align_lines [Confidence: 1.00]
def align_lines(lines):
    width = 0
    for line in lines:
        if len(line) > width:
            width = len(line)
    border = "*" * (width + 2)
    collected = [border]
    lean_left = True
    for line in lines:
        room = width - len(line)
        if room % 2 == 0:
            start = room // 2
        elif lean_left:
            start = room // 2
            lean_left = False
        else:
            start = room - room // 2
            lean_left = True
        collected.append("*" + " " * start + line + " " * (room - start) + "*")
    collected.append(border)
    return collected

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("\n".join(align_lines(read_input())) + "\n")


if __name__ == "__main__":
    main()

