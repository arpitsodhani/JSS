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
    pieces = [border]
    lean_left = True
    for line in lines:
        room = width - len(line)
        if room % 2 == 0:
            low = room // 2
        elif lean_left:
            low = room // 2
            lean_left = False
        else:
            low = room - room // 2
            lean_left = True
        pieces.append("*" + " " * low + line + " " * (room - low) + "*")
    pieces.append(border)
    return pieces


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(align_lines(read_input())) + "\n")


if __name__ == "__main__":
    main()
