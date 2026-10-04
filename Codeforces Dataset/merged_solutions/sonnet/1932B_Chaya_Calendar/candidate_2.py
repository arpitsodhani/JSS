import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: doom_year :: (signs: list[int]) -> int ---
def doom_year(signs):
    year = 0
    for step in signs:
        year = (year // step + 1) * step
    return year


# --- clause: main :: () -> None ---
def main():
    out = []
    for signs in read_input():
        out.append(doom_year(signs))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
