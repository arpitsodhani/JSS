import sys

def restore(n, segs):
    masks = []
    lens = []
    starts = []

    for arr in segs:
        mask = 0
        for x in arr:
            mask |= 1 << (x - 1)
        masks.append(mask)
        lens.append(len(arr))
        if len(arr) == 2:
            starts.extend(arr)

    seen = [False] * (n + 1)
    candidates = []
    for x in starts:
        if not seen[x]:
            seen[x] = True
            candidates.append(x)

    for first in candidates:
        perm = [first]
        used = 1 << (first - 1)
        pref = [0, used]
        remaining = list(range(n - 1))

        ok = True
        while len(perm) < n:
            m = len(perm)
            found = -1
            add = -1

            for pos, idx in enumerate(remaining):
                k = lens[idx]
                if k - 1 > m:
                    continue

                outside = masks[idx] & ~used
                if outside.bit_count() != 1:
                    continue

                suffix = used ^ pref[m - (k - 1)]
                if (masks[idx] & used) == suffix:
                    found = pos
                    add = outside.bit_length()
                    break

            if found == -1:
                ok = False
                break

            perm.append(add)
            used |= 1 << (add - 1)
            pref.append(used)
            remaining[found] = remaining[-1]
            remaining.pop()

        if ok and not remaining:
            return perm

    return list(range(1, n + 1))

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ptr = 1
    ans = []

    for _ in range(t):
        n = data[ptr]
        ptr += 1
        segs = []
        for _ in range(n - 1):
            k = data[ptr]
            ptr += 1
            segs.append(data[ptr:ptr + k])
            ptr += k
        ans.append(" ".join(map(str, restore(n, segs))))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
