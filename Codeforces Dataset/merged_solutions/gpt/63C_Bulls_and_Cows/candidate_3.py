# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from itertools import permutations

    data = sys.stdin.read().split()
    n = int(data[0])
    queries = []

    idx = 1
    for _ in range(n):
        guess = data[idx].zfill(4)
        bulls = int(data[idx + 1])
        cows = int(data[idx + 2])
        queries.append((guess, bulls, cows))
        idx += 3

    ans = []

    for p in permutations("0123456789", 4):
        s = "".join(p)
        ok = True
        ss = set(s)

        for guess, b, c in queries:
            bulls = sum(s[i] == guess[i] for i in range(4))
            cows = len(ss & set(guess)) - bulls
            if bulls != b or cows != c:
                ok = False
                break

        if ok:
            ans.append(s)
            if len(ans) > 1:
                break

    if len(ans) == 0:
        print("Incorrect data")
    elif len(ans) == 1:
        print(ans[0])
    else:
        print("Need more data")

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
