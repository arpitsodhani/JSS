import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 * i + 2] for i in range(t)]


# --- clause: spread_letters :: (s: bytes) -> str ---
def spread_letters(s):
    buckets = [[] for _ in range(26)]
    for ch in s:
        buckets[ch - 97].append(chr(ch))
    tallest = 0
    for bucket in buckets:
        if len(bucket) > tallest:
            tallest = len(bucket)
    out = []
    for level in range(tallest):
        for bucket in buckets:
            if level < len(bucket):
                out.append(bucket[level])
    return "".join(out)


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(spread_letters(s))
    print("\n".join(out))


if __name__ == "__main__":
    main()
