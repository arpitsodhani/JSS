import sys


# --- clause: read_input :: () -> list[bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    rows = []
    for i in range(t):
        rows.append(data[2 * i + 2])
    return rows


# --- clause: spread_letters :: (s: bytes) -> str ---
def spread_letters(s):
    buckets = [[] for _ in range(26)]
    for ch in s:
        buckets[ch - 97].append(chr(ch))
    tallest = max(len(bucket) for bucket in buckets)
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
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
