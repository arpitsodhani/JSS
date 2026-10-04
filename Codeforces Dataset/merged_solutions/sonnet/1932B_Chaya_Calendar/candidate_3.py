import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: doom_year :: (signs: list[int]) -> int ---
def doom_year(signs):
    year = 0
    for jump in signs:
        year = (year // jump + 1) * jump
    return year


# --- clause: main :: () -> None ---
def main():
    out = []
    for signs in read_input():
        out.append(doom_year(signs))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
