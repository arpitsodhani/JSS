import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    lines = sys.stdin.read().split("\n")
    count = int(lines[0])
    return [line.rstrip("\r") for line in lines[1:1 + count]]


# --- clause: whose_line :: (line: str) -> str ---
def whose_line(line):
    if line.startswith("miao.") and line.endswith("lala."):
        return "OMG>.< I don't know!"
    if line.endswith("lala."):
        return "Freda's"
    if line.startswith("miao."):
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
