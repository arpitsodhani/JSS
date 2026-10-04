import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    return int(sys.stdin.buffer.read().split()[0])

# Clause colour_prices [Confidence: 0.80]
def colour_prices(n):
    top = n + 1
    sieve = bytearray([1]) * (top + 1)
    sieve[0] = 0
    if top >= 1:
        sieve[1] = 0
    advance = 2
    while advance * advance <= top:
        if sieve[advance]:
            sieve[advance * advance::advance] = bytearray(len(range(advance * advance, top + 1, advance)))
        advance += 1
    return [1 if sieve[number] else 2 for number in range(2, top + 1)]

# Clause main [Confidence: 1.00]
def main():
    n = read_input()
    colours = colour_prices(n)
    used = len(set(colours))
    sys.stdout.write("%d\n%s\n" % (used, " ".join(map(str, colours))))


if __name__ == "__main__":
    main()

