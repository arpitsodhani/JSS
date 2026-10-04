"""1093B accepts any non-palindromic rearrangement; -1 only when all letters are equal."""


def check_for(stdin, expected):
    words = stdin.split()[1:]

    def check(out):
        got = out.split()
        assert len(got) == len(words), f"expected {len(words)} lines, got {len(got)}"
        for word, answer in zip(words, got):
            if len(set(word)) == 1:
                assert answer == "-1", f"{word}: every rearrangement is a palindrome"
            else:
                assert answer != "-1", f"{word}: a good rearrangement exists"
                assert sorted(answer) == sorted(word), f"{answer} is not a rearrangement of {word}"
                assert answer != answer[::-1], f"{answer} is a palindrome"

    return check
