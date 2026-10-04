import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(data[1:1 + t])


# --- clause: longest_good :: (s: bytes) -> int ---
def longest_good(s):
    best = 0
    for first in range(10):
        for second in range(10):
            want = 48 + first
            other = 48 + second
            length = 0
            expect = want
            for ch in s:
                if ch == expect:
                    length += 1
                    expect = other if expect == want else want
            if first != second:
                length -= length % 2
            if length > best:
                best = length
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(str(len(s) - longest_good(s)))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
