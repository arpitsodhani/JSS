"""357B accepts any colouring in which every dance shows all three colours."""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    m = data[1]
    dances = [tuple(data[2 + 3 * i:5 + 3 * i]) for i in range(m)]

    def check(out):
        colors = [int(v) for v in out.split()]
        assert len(colors) == n, f"expected {n} colours, got {len(colors)}"
        assert all(c in (1, 2, 3) for c in colors), "colours must be 1, 2 or 3"
        for idx, trio in enumerate(dances, start=1):
            worn = {colors[d - 1] for d in trio}
            assert worn == {1, 2, 3}, f"dance {idx} wears {sorted(worn)}"

    return check
