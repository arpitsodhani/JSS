import sys

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    p = 1
    out = []

    for _ in range(t):
        n = int(data[p])
        m = int(data[p + 1])
        p += 2

        s = bytearray(data[p])
        p += 1

        inds = [int(data[p + i]) - 1 for i in range(m)]
        p += m

        c = data[p]
        p += 1

        positions = sorted(set(inds))
        chars = sorted(c)

        for idx, ch in zip(positions, chars):
            s[idx] = ch

        out.append(s.decode())

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
