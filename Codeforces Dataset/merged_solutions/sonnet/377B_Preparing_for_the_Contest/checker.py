"""377B accepts any schedule that fixes every bug in the fewest days.

The printed assignment is checked for ability and budget, and its number of
days is compared with the reference schedule's.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m, s = data[0], data[1], data[2]
    bugs = data[3:3 + m]
    skill = data[3 + m:3 + m + n]
    price = data[3 + m + n:3 + m + 2 * n]
    lines = [line.strip() for line in expected.split("\n") if line.strip()]
    possible = lines[0].upper() == "YES"

    def days_of(plan):
        load = {}
        for who in plan:
            load[who] = load.get(who, 0) + 1
        return max(load.values())

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0].upper() == "NO", "printed a schedule where none exists"
            return
        assert rows[0].upper() == "YES", "a schedule exists but NO was printed"
        plan = [int(v) for v in rows[1].split()]
        assert len(plan) == m, f"expected {m} assignments, got {len(plan)}"
        for j in range(m):
            who = plan[j]
            assert 1 <= who <= n, f"student {who} out of range"
            assert skill[who - 1] >= bugs[j], f"student {who} cannot fix bug {j + 1}"
        spent = sum(price[who - 1] for who in set(plan))
        assert spent <= s, f"the schedule costs {spent}, the budget is {s}"
        best = days_of([int(v) for v in lines[1].split()])
        assert days_of(plan) <= best, f"takes {days_of(plan)} days, best is {best}"

    return check
