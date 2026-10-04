"""549B accepts any guest list that makes every received count differ from Igor's
guess; -1 only when no such list exists."""


def check_for(stdin, expected):
    tokens = stdin.split()
    n = int(tokens[0])
    lists = tokens[1:1 + n]
    guess = [int(v) for v in tokens[1 + n:1 + n + n]]

    def check(out):
        got = [int(v) for v in out.split()]
        if len(got) == 1 and got[0] == -1:
            raise AssertionError("printed -1, but a guest list always exists here")
        m = got[0]
        guests = got[1:]
        assert len(guests) == m, f"promised {m} guests, listed {len(guests)}"
        assert len(set(guests)) == m, "a guest is listed twice"
        received = [0] * n
        for g in guests:
            assert 1 <= g <= n, f"employee {g} does not exist"
            row = lists[g - 1]
            for j in range(n):
                if row[j] == "1":
                    received[j] += 1
        for j in range(n):
            assert received[j] != guess[j], (
                f"employee {j + 1} received {received[j]}, matching Igor's guess")

    return check
