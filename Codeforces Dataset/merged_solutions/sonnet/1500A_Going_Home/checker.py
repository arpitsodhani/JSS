"""1500A accepts any four distinct indices with a_x + a_y = a_z + a_w.

Whether such indices exist is recomputed here by scanning pairs, so the printed
verdict is checked as well as the printed indices.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    a = data[1:1 + n]
    seen = {}
    possible = False
    for j in range(n):
        for i in range(j):
            key = a[i] + a[j]
            if key in seen:
                x, y = seen[key]
                if x not in (i, j) and y not in (i, j):
                    possible = True
                    break
            else:
                seen[key] = (i, j)
        if possible:
            break

    def check(out):
        words = out.split()
        if not possible:
            assert words[0].upper() == "NO", f"a quadruple exists, printed {words[0]}"
            return
        assert words[0].upper() == "YES", f"expected YES, got {words[0]}"
        idx = [int(v) for v in words[1:5]]
        assert len(set(idx)) == 4, "the indices must be distinct"
        assert all(1 <= v <= n for v in idx), "index out of range"
        x, y, z, w = idx
        assert a[x - 1] + a[y - 1] == a[z - 1] + a[w - 1], "the sums differ"

    return check
