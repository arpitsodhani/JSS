"""2005A accepts any vowel string with the fewest palindromic subsequences.

The printed string is scored with the standard palindromic-subsequence count
and compared against the reference string's score.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    sizes = data[1:1 + data[0]]
    reference = [line.strip() for line in expected.split("\n") if line.strip()]

    def palindromes(s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                if s[i] == s[j]:
                    dp[i][j] += dp[i + 1][j - 1] + 1
        return dp[0][n - 1]

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        assert len(rows) == len(sizes), f"expected {len(sizes)} lines, got {len(rows)}"
        for case in range(len(sizes)):
            word = rows[case]
            assert len(word) == sizes[case], f"case {case + 1}: length {len(word)}, expected {sizes[case]}"
            assert set(word) <= set("aeiou"), f"case {case + 1}: only vowels are allowed"
            best = palindromes(reference[case])
            here = palindromes(word)
            assert here <= best, f"case {case + 1}: {here} palindromic subsequences, best is {best}"

    return check
