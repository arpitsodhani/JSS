"""863E accepts any redundant TV set, so the printed index is checked itself."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    spans = [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)]
    possible = int(expected.split()[0]) != -1

    def covered(skip):
        pieces = []
        for i in range(n):
            if i == skip:
                continue
            pieces.append(spans[i])
        pieces.sort()
        total = 0
        low = None
        high = None
        for l, r in pieces:
            if low is None:
                low, high = l, r
            elif l <= high + 1:
                if r > high:
                    high = r
            else:
                total += high - low + 1
                low, high = l, r
        if low is not None:
            total += high - low + 1
        return total

    def check(out):
        answer = int(out.split()[0])
        if not possible:
            assert answer == -1, "printed an index but no TV is redundant"
            return
        assert answer != -1, "a redundant TV exists"
        assert 1 <= answer <= n, "index out of range"
        assert covered(answer - 1) == covered(-1), f"TV {answer} is not redundant"

    return check
