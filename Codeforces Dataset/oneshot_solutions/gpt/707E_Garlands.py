import sys
from array import array

def main():
    data = sys.stdin.buffer.read()
    pos = 0
    size = len(data)

    def next_int():
        nonlocal pos
        while pos < size and data[pos] <= 32:
            pos += 1
        val = 0
        while pos < size and data[pos] > 32:
            val = val * 10 + (data[pos] - 48)
            pos += 1
        return val

    def next_word_first():
        nonlocal pos
        while pos < size and data[pos] <= 32:
            pos += 1
        c = data[pos]
        while pos < size and data[pos] > 32:
            pos += 1
        return c

    n = next_int()
    m = next_int()
    k = next_int()

    garlands = []
    for _ in range(k):
        length = next_int()
        xs = array('H')
        ys = array('H')
        ws = array('q')
        for _ in range(length):
            xs.append(next_int())
            ys.append(next_int())
            ws.append(next_int())
        garlands.append((xs, ys, ws))

    q = next_int()
    events = array('i')
    x1s = array('H')
    y1s = array('H')
    x2s = array('H')
    y2s = array('H')

    ask_count = 0
    for _ in range(q):
        c = next_word_first()
        if c == 83:
            g = next_int() - 1
            events.append(-g - 1)
        else:
            x1s.append(next_int())
            y1s.append(next_int())
            x2s.append(next_int())
            y2s.append(next_int())
            events.append(ask_count)
            ask_count += 1

    data = b''

    contrib = array('q', [0]) * (ask_count * k)

    if ask_count:
        for g, (xs, ys, ws) in enumerate(garlands):
            points = sorted(zip(xs, ys, ws))
            queries = []
            for qi in range(ask_count):
                x1 = x1s[qi]
                y1 = y1s[qi]
                x2 = x2s[qi]
                y2 = y2s[qi]
                queries.append((x2, y2, qi, 1))
                if x1 > 1:
                    queries.append((x1 - 1, y2, qi, -1))
                if y1 > 1:
                    queries.append((x2, y1 - 1, qi, -1))
                if x1 > 1 and y1 > 1:
                    queries.append((x1 - 1, y1 - 1, qi, 1))

            queries.sort()
            bit = [0] * (m + 1)
            vals = [0] * ask_count
            p = 0
            plen = len(points)

            for xlim, ylim, qi, sign in queries:
                while p < plen and points[p][0] <= xlim:
                    _, yy, ww = points[p]
                    j = yy
                    while j <= m:
                        bit[j] += ww
                        j += j & -j
                    p += 1

                s = 0
                j = ylim
                while j > 0:
                    s += bit[j]
                    j -= j & -j

                vals[qi] += s if sign == 1 else -s

            for qi, val in enumerate(vals):
                if val:
                    contrib[qi * k + g] = val

    on = bytearray([1]) * k
    out = []

    for ev in events:
        if ev < 0:
            g = -ev - 1
            on[g] ^= 1
        else:
            base = ev * k
            total = 0
            for g in range(k):
                if on[g]:
                    total += contrib[base + g]
            out.append(str(total))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()
