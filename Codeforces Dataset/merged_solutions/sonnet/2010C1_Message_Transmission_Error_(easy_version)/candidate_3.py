import sys


# --- clause: read_input :: () -> str ---
def read_input():
    data = sys.stdin.buffer.read().split()
    word = data[0].decode()
    return word


# --- clause: find_source :: (text: str) -> str ---
def find_source(text):
    total = len(text)
    for size in range(total - 1, total // 2, -1):
        overlap = 2 * size - total
        if overlap < 1 or overlap >= size:
            continue
        if text[:size] == text[total - size:]:
            return "YES\n" + text[:size]
    return "NO"


# --- clause: main :: () -> None ---
def main():
    print(find_source(read_input()))


if __name__ == "__main__":
    main()
