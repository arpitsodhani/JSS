import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()


# --- clause: transform :: (text: str) -> str ---
def transform(text):
    vowels = ("a", "o", "y", "e", "u", "i")
    out = []
    for ch in text.lower():
        if ch in vowels:
            continue
        out.append(".%s" % ch)
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(transform(read_input()) + "\n")


if __name__ == "__main__":
    main()
