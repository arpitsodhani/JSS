"""346B accepts any longest common subsequence of s1 and s2 avoiding virus.

The checker recomputes the best length with its own dp over (i, j, kmp state)
and then verifies the printed string is a common subsequence of that length
which does not contain virus.
"""


def check_for(stdin, expected):
    s1, s2, virus = stdin.split()[:3]

    def best_length():
        n1, n2, v = len(s1), len(s2), len(virus)
        fail = [0] * v
        border = 0
        for i in range(1, v):
            while border and virus[i] != virus[border]:
                border = fail[border - 1]
            if virus[i] == virus[border]:
                border += 1
            fail[i] = border
        def step(state, ch):
            while state and virus[state] != ch:
                state = fail[state - 1]
            return state + 1 if virus[state] == ch else 0
        dp = [[[-1] * v for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0][0] = 0
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                for k in range(v):
                    cur = dp[i][j][k]
                    if cur < 0:
                        continue
                    if i < n1 and dp[i + 1][j][k] < cur:
                        dp[i + 1][j][k] = cur
                    if j < n2 and dp[i][j + 1][k] < cur:
                        dp[i][j + 1][k] = cur
                    if i < n1 and j < n2 and s1[i] == s2[j]:
                        nk = step(k, s1[i])
                        if nk < v and dp[i + 1][j + 1][nk] < cur + 1:
                            dp[i + 1][j + 1][nk] = cur + 1
        return max(dp[n1][n2])

    target = best_length()

    def is_subsequence(t, s):
        it = iter(s)
        return all(ch in it for ch in t)

    def check(out):
        text = out.strip()
        if target == 0:
            assert text == "0", f"no valid subsequence exists, printed {text!r}"
            return
        assert text != "0", f"a subsequence of length {target} exists"
        assert len(text) == target, f"printed length {len(text)}, best is {target}"
        assert is_subsequence(text, s1), "not a subsequence of s1"
        assert is_subsequence(text, s2), "not a subsequence of s2"
        assert virus not in text, "the answer contains the virus"

    return check
