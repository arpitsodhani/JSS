import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return bytes(data[0]).decode()


# --- clause: transform :: (text: str) -> str ---
def transform(text):
    vowels = "aoyeui"
    out = []
    lowered = text.lower()
    for i in range(len(lowered)):
        ch = lowered[i]
        if ch not in vowels:
            out.append(".")
            out.append(ch)
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    text = read_input()
    sys.stdout.write(transform(text) + "\n")


if __name__ == "__main__":
    main()
