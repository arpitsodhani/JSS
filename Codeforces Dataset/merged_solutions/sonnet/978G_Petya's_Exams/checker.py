"""978G accepts any timetable that fits every exam's preparation days.

Feasibility is recomputed with an earliest-deadline-first greedy, which is
optimal here, and then the printed plan is validated day by day.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n, m = data[0], data[1]
    exams = [(data[2 + 3 * i], data[3 + 3 * i], data[4 + 3 * i]) for i in range(m)]
    plan = [0] * (n + 1)
    for s, d, c in exams:
        plan[d] = m + 1
    feasible = True
    for index in sorted(range(m), key=lambda i: exams[i][1]):
        s, d, c = exams[index]
        left = c
        for slot in range(s, d):
            if left == 0:
                break
            if plan[slot] == 0:
                plan[slot] = index + 1
                left -= 1
        if left:
            feasible = False
            break

    def check(out):
        text = out.split()
        if not feasible:
            assert text == ["-1"], f"no timetable exists, printed {text[:6]}"
            return
        assert text != ["-1"], "a timetable exists but -1 was printed"
        days = [int(v) for v in text]
        assert len(days) == n, f"expected {n} days, got {len(days)}"
        for s, d, c in exams:
            assert days[d - 1] == m + 1, f"day {d} must hold an exam"
        for index, (s, d, c) in enumerate(exams, start=1):
            got = [j + 1 for j, v in enumerate(days) if v == index]
            assert len(got) == c, f"exam {index}: {len(got)} preparation days, needs {c}"
            for j in got:
                assert s <= j < d, f"exam {index}: day {j} outside [{s}, {d - 1}]"
        exam_days = {d for _s, d, _c in exams}
        for j, v in enumerate(days, start=1):
            if v == m + 1:
                assert j in exam_days, f"day {j} marked as an exam but none is scheduled"
            else:
                assert 0 <= v <= m, f"day {j} has label {v}"

    return check
