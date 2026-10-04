import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    return data[1:1 + data[0]]

# Clause cut_segments [Confidence: 1.00]
def cut_segments(a):
    parts = []
    known = set()
    opening = 1
    for i in range(len(a)):
        if a[i] in known:
            parts.append((opening, i + 1))
            opening = i + 2
            known = set()
        else:
            known.add(a[i])
    if parts:
        parts[-1] = (parts[-1][0], len(a))
    return parts

# Clause main [Confidence: 1.00]
def main():
    parts = cut_segments(read_input())
    if not parts:
        sys.stdout.write("-1\n")
    else:
        out = [str(len(parts))]
        for left, right in parts:
            out.append("%d %d" % (left, right))
        sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

