# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    vowels = "aeiou"
    ans = []

    for n in data[1:1 + t]:
        q, r = divmod(n, 5)
        s = []
        for i in range(5):
            s.append(vowels[i] * (q + (i < r)))
        ans.append("".join(s))

    print("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
