import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return str(data[0], "ascii")


# --- clause: find_source :: (text: str) -> str ---
def find_source(text):
    total = len(text)
    for overlap in range(1, total):
        if (total + overlap) % 2:
            continue
        size = (total + overlap) // 2
        if size <= overlap or size >= total:
            continue
        if text[:size] == text[total - size:]:
            return "YES\n" + text[:size]
    return "NO"


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%s\n" % find_source(read_input()))


if __name__ == "__main__":
    main()
