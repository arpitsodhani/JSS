# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def best_bounds(a):
    prefix = [0] * (len(a) + 1)
    marked = []
    for i, v in enumerate(a):
        prefix[i + 1] = prefix[i] + v
        if v > 1:
            marked.append(i)

    if marked == []:
        return "1 1"

    if len(marked) > 70:
        return "{} {}".format(marked[0] + 1, marked[-1] + 1)

    gain = 0
    answer = [1, 1]
    size = len(marked)

    for begin in range(size):
        product = 1
        l = marked[begin]
        for end in range(begin, size):
            r = marked[end]
            product = product * a[r]
            total = prefix[r + 1] - prefix[l]
            candidate = product - total
            if candidate > gain:
                gain = candidate
                answer[0] = l + 1
                answer[1] = r + 1

    return str(answer[0]) + " " + str(answer[1])

def main():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    k = 1
    output = []
    for _ in range(t):
        n = int(raw[k])
        k += 1
        arr = [int(x) for x in raw[k:k + n]]
        k += n
        output.append(best_bounds(arr))
    sys.stdout.write("\n".join(output))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
