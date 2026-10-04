import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(t)]


# --- clause: count_marks :: (s: str) -> int ---
def count_marks(s):
    total = s.count("w")
    for chunk in s.split("w"):
        total += len(chunk) // 2
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(count_marks(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
