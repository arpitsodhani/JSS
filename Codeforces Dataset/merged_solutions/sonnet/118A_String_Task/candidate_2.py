import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return str(data[0], "ascii")


# --- clause: transform :: (text: str) -> str ---
def transform(text):
    vowels = set("aoyeui")
    out = []
    for ch in text.lower():
        if ch not in vowels:
            out.append("." + ch)
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % transform(read_input()))


if __name__ == "__main__":
    main()
