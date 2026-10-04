import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return [data[2 + 2 * i].decode() for i in range(t)]

# Clause chain_lengths [Confidence: 1.00]
def chain_lengths(s):
    n = len(s)
    right_r = [0] * (n + 2)
    right_l = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        right_r[i] = 1 + right_l[i + 1] if s[i] == "R" else 0
        right_l[i] = 1 + right_r[i + 1] if s[i] == "L" else 0
    left_l = [0] * (n + 1)
    left_r = [0] * (n + 1)
    for j in range(n):
        back_l = left_l[j - 1] if j else 0
        back_r = left_r[j - 1] if j else 0
        left_l[j] = 1 + back_r if s[j] == "L" else 0
        left_r[j] = 1 + back_l if s[j] == "R" else 0
    return right_r, left_l

# Clause city_answers [Confidence: 1.00]
def city_answers(s, ahead, behind):
    n = len(s)
    collected = []
    for city in range(n + 1):
        stop = ahead[city] if city < n else 0
        left = behind[city - 1] if city else 0
        collected.append(1 + left + stop)
    return collected

# Clause main [Confidence: 1.00]
def main():
    collected = []
    for s in read_input():
        ahead, behind = chain_lengths(s)
        collected.append(" ".join(map(str, city_answers(s, ahead, behind))))
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()

