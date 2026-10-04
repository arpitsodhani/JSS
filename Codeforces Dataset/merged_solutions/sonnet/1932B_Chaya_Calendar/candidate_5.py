import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: doom_year :: (signs: list[int]) -> int ---
def doom_year(signs):
    year = 0
    for stride in signs:
        year = (year // stride + 1) * stride
    return year


# --- clause: main :: () -> None ---
def main():
    out = []
    for signs in read_input():
        out.append(doom_year(signs))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
