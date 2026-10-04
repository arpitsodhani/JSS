import sys


# --- clause: read_input :: () -> bytes ---
def read_input():
    data = sys.stdin.buffer.read().split()
    return data[0][:]


# --- clause: longest_beautiful :: (s: str) -> int ---
def longest_beautiful(s):
    first = 0
    middle = 0
    last = 0
    for ch in s:
        is_a = 1 if ch == 97 else 0
        new_first = first + is_a
        new_middle = (first if first > middle else middle) + (1 - is_a)
        new_last = (middle if middle > last else last) + is_a
        first, middle, last = new_first, new_middle, new_last
    best = first
    if middle > best:
        best = middle
    if last > best:
        best = last
    return best


# --- clause: main :: () -> None ---
def main():
    text = read_input()
    sys.stdout.write(str(longest_beautiful(text)) + "\n")


if __name__ == "__main__":
    main()
