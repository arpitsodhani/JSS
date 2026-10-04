# CLAUSE: setup_environment
from sys import stdin, stdout

MOD = 10 ** 9 + 7

# CLAUSE: solve_logic
def main():
    nums = [int(x) for x in stdin.buffer.read().split()]
    t = nums[0]
    index = 1
    packed = []
    max_n = 0

    for _ in range(t):
        n, k = nums[index], nums[index + 1]
        index += 2
        segment = nums[index:index + n]
        index += n
        one_count = 0
        for bit in segment:
            one_count += bit
        packed.append({"n": n, "k": k, "one": one_count})
        if max_n < n:
            max_n = n

    fac = [1]
    for i in range(1, max_n + 1):
        fac.append(fac[-1] * i % MOD)

    inv = [1] * (max_n + 1)
    inv[-1] = pow(fac[-1], MOD - 2, MOD)
    for i in range(max_n - 1, -1, -1):
        inv[i] = inv[i + 1] * (i + 1) % MOD

    answers = []
    for item in packed:
        n = item["n"]
        k = item["k"]
        one = item["one"]
        zero = n - one
        need = (k + 1) // 2
        ways = 0

        for z in range(0, min(zero, k - need) + 1):
            o = k - z
            if o <= one:
                left = fac[one] * inv[o] % MOD * inv[one - o] % MOD
                right = fac[zero] * inv[z] % MOD * inv[zero - z] % MOD
                ways = (ways + left * right) % MOD

        answers.append(str(ways))

    stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
