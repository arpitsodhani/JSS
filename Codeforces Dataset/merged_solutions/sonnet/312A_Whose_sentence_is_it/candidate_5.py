import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    lines = sys.stdin.read().split("\n")
    count = int(lines[0])
    return [line.rstrip("\r") for line in lines[1:1 + count]]


# --- clause: whose_line :: (line: str) -> str ---
def whose_line(line):
    freda = len(line) >= 5 and line[-5:] == "lala."
    rainbow = len(line) >= 5 and line[0:5] == "miao."
    if freda and rainbow:
        return "OMG>.< I don't know!"
    if freda:
        return "Freda's"
    if rainbow:
        return "Rainbow's"
    return "OMG>.< I don't know!"


# --- clause: main :: () -> None ---
def main():
    out = []
    for line in read_input():
        out.append(whose_line(line))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
