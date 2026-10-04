import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    text = sys.stdin.read()
    if text.endswith("\n"):
        text = text[:-1]
    return [line.rstrip("\r") for line in text.split("\n")]


# --- clause: align_lines :: (lines: list[str]) -> list[str] ---
def align_lines(lines):
    width = 0
    for line in lines:
        if len(line) > width:
            width = len(line)
    border = "*" * (width + 2)
    written = [border]
    lean_left = True
    for line in lines:
        room = width - len(line)
        if room % 2 == 0:
            begin = room // 2
        elif lean_left:
            begin = room // 2
            lean_left = False
        else:
            begin = room - room // 2
            lean_left = True
        written.append("*" + " " * begin + line + " " * (room - begin) + "*")
    written.append(border)
    return written


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(align_lines(read_input())) + "\n")


if __name__ == "__main__":
    main()
