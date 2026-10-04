import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    lines = sys.stdin.read().split("\n")
    count = int(lines[0])
    return [line.rstrip("\r") for line in lines[1:1 + count]]


# --- clause: whose_line :: (line: str) -> str ---
def whose_line(line):
    freda = line.endswith("lala.")
    rainbow = line.startswith("miao.")
    if freda and not rainbow:
        return "Freda's"
    if rainbow and not freda:
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
