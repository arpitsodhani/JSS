"""3A accepts any shortest king walk from s to t."""


def check_for(stdin, expected):
    rows = stdin.split()
    start = rows[0]
    goal = rows[1]
    best = int(expected.split("\n")[0])

    def check(out):
        lines = [line.strip() for line in out.split("\n") if line.strip()]
        count = int(lines[0])
        assert count == best, f"used {count} moves, the fewest is {best}"
        x = ord(start[0]) - 96
        y = int(start[1])
        for i in range(count):
            move = lines[1 + i]
            assert 1 <= len(move) <= 2, "a move must be one or two letters"
            for ch in move:
                if ch == "L":
                    x -= 1
                elif ch == "R":
                    x += 1
                elif ch == "U":
                    y += 1
                elif ch == "D":
                    y -= 1
                else:
                    raise AssertionError("unknown direction")
            assert 1 <= x <= 8 and 1 <= y <= 8, "the king left the board"
        assert x == ord(goal[0]) - 96 and y == int(goal[1]), "the king did not arrive"

    return check
