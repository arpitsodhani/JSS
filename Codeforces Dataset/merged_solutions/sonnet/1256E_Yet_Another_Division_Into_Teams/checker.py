"""1256E accepts any division reaching the smallest total diversity.

Every team must hold at least three students, and the sum of per-team spans has
to match both the printed total and the reference one.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    skills = data[1:1 + n]
    best = int(expected.split()[0])

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        total, teams = (int(v) for v in rows[0].split())
        labels = [int(v) for v in rows[1].split()]
        assert len(labels) == n, f"expected {n} labels, got {len(labels)}"
        assert all(1 <= v <= teams for v in labels), "a team number is out of range"
        groups = {}
        for i in range(n):
            groups.setdefault(labels[i], []).append(skills[i])
        assert len(groups) == teams, f"printed {teams} teams, used {len(groups)}"
        spread = 0
        for members in groups.values():
            assert len(members) >= 3, "a team has fewer than three students"
            spread += max(members) - min(members)
        assert spread == total, f"the division costs {spread}, printed {total}"
        assert total == best, f"total {total}, the smallest is {best}"

    return check
