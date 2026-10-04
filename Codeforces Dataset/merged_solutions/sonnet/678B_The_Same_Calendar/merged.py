import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause is_leap [Confidence: 1.00]
def is_leap(year):
    if year % 400 == 0:
        return True
    return year % 4 == 0 and year % 100 != 0

# Clause next_same [Confidence: 1.00]
def next_same(year):
    shift = 0
    advance = year
    while True:
        shift = (shift + (366 if is_leap(advance) else 365)) % 7
        advance += 1
        if shift == 0 and is_leap(advance) == is_leap(year):
            return advance

# Clause main [Confidence: 1.00]
def main():
    sys.stdout.write("%d\n" % next_same(read_input()))


if __name__ == "__main__":
    main()

