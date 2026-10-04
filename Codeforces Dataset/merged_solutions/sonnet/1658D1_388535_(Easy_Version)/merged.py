# Clause setup_environment [Confidence: 0.40]
import sys


# Clause solve_logic [Confidence: 0.60]
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    at = 1
    total = data[0]
    output = []
    for _ in range(total):
        l = data[at]
        r = data[at + 1]
        at += 2
        size = r - l + 1
        arr = data[at:at + size]
        at += size
        cap = 1 << (max(arr + [l, r]).bit_length())
        answer = 0
        x = 0
        while x < cap:
            marks = [0] * size
            good = True
            for v in arr:
                y = v ^ x
                j = y - l
                if j < 0 or j >= size or marks[j]:
                    good = False
                    break
                marks[j] = 1
            if good:
                answer = x
                break
            x += 1
        output.append(str(answer))
    print("\n".join(output))


# Clause finish_program [Confidence: 0.60]
if __name__ == "__main__":
    main()


