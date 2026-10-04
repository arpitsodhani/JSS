import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0].decode()


# --- clause: find_source :: (text: str) -> str ---
def find_source(text):
    total = len(text)
    for size in range((total + 2) // 2, total):
        overlap = 2 * size - total
        if overlap < 1 or overlap >= size:
            continue
        if text[:size] == text[total - size:]:
            return "YES\n" + text[:size]
    return "NO"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(find_source(read_input()) + "\n")


if __name__ == "__main__":
    main()
