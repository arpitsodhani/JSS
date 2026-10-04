"""1264B accepts any beautiful arrangement using every supplied number."""


def check_for(stdin, expected):
    counts = [int(v) for v in stdin.split()]
    total = sum(counts)

    def possible():
        for start in range(4):
            left = list(counts)
            if not left[start]:
                continue
            left[start] -= 1
            cur = start
            made = 1
            while True:
                if cur and left[cur - 1]:
                    cur -= 1
                elif cur < 3 and left[cur + 1]:
                    cur += 1
                else:
                    break
                left[cur] -= 1
                made += 1
            if made == total:
                return True
        return False

    feasible = possible()

    def check(out):
        got = out.split()
        if got[0].upper() == "NO":
            assert not feasible, "printed NO but a sequence exists"
            return
        assert feasible, "printed a sequence but none exists"
        values = [int(v) for v in got[1:]]
        assert len(values) == total, f"expected {total} numbers, got {len(values)}"
        used = [0] * 4
        for v in values:
            assert 0 <= v <= 3, f"{v} outside 0..3"
            used[v] += 1
        assert used == counts, f"used {used}, supplied {counts}"
        for i in range(total - 1):
            assert abs(values[i] - values[i + 1]) == 1, (
                f"positions {i + 1} and {i + 2} differ by {abs(values[i] - values[i + 1])}")

    return check
