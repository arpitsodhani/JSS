# Clause setup_environment [Confidence: 0.60]
import sys

MOD = 998244353


# Clause solve_logic [Confidence: 0.80]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    max_n = 0

    for _ in range(t):
        n = data[pos]
        pos += 1
        arr = data[pos:pos + n]
        pos += n
        cases.append(arr)
        if n > max_n:
            max_n = n

    fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % MOD

    answers = []
    for arr in cases:
        arr.sort()
        n = len(arr)
        top = arr[-1]
        second = arr[-2]

        if top == second:
            answers.append(str(fact[n]))
        elif top - second > 1:
            answers.append("0")
        else:
            need = top - 1
            cnt = arr.count(need)
            invalid = fact[n] * pow(cnt + 1, MOD - 2, MOD) % MOD
            answers.append(str((fact[n] - invalid) % MOD))

    sys.stdout.write("\n".join(answers))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


