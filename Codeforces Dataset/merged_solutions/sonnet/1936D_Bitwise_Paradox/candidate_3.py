# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def minimum_beauty(a, b, target, left, right):
    answer = 10 ** 30
    start = left
    while start <= right:
        value_or = 0
        value_max = 0
        end = start
        while end <= right:
            value_or = value_or | b[end]
            if a[end] > value_max:
                value_max = a[end]
            if value_or >= target:
                if value_max < answer:
                    answer = value_max
                break
            end += 1
        start += 1
    if answer == 10 ** 30:
        return -1
    return answer

def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    pos = 0
    n, q, v = tokens[pos], tokens[pos + 1], tokens[pos + 2]
    pos += 3
    a = [0] + tokens[pos:pos + n]
    pos += n
    b = [0] + tokens[pos:pos + n]
    pos += n
    out = []
    for _ in range(q):
        kind = tokens[pos]
        pos += 1
        if kind == 1:
            index, new_value = tokens[pos], tokens[pos + 1]
            pos += 2
            b[index] = new_value
        else:
            left, right = tokens[pos], tokens[pos + 1]
            pos += 2
            out.append(str(minimum_beauty(a, b, v, left, right)))
    sys.stdout.write("\n".join(out))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
