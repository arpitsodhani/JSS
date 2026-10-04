import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []

    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        ones = 0
        inv = 0
        for x in a:
            if x == 1:
                ones += 1
            else:
                inv += ones

        total_zeros = n - ones
        ones_before = 0
        zeros_seen = 0
        best_delta = 0

        for x in a:
            if x == 0:
                zeros_after = total_zeros - zeros_seen - 1
                best_delta = max(best_delta, zeros_after - ones_before)
                zeros_seen += 1
            else:
                zeros_after = total_zeros - zeros_seen
                best_delta = max(best_delta, ones_before - zeros_after)
                ones_before += 1

        out.append(str(inv + best_delta))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
