# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    words = data[1:]
    groups = [[] for _ in range(n)]

    for idx, word in enumerate(words):
        groups[len(word)].append((idx, word))

    left = groups[n - 1][0][1]
    right = groups[n - 1][1][1]

    def check(source):
        answer = [""] * (2 * n - 2)
        for length in range(1, n):
            first, second = groups[length]
            prefix = source[:length]
            suffix = source[n - length:]
            if first[1] == prefix and second[1] == suffix:
                answer[first[0]] = "P"
                answer[second[0]] = "S"
            elif first[1] == suffix and second[1] == prefix:
                answer[first[0]] = "S"
                answer[second[0]] = "P"
            else:
                return None
        return "".join(answer)

    for source in (left + right[-1], right + left[-1]):
        result = check(source)
        if result is not None:
            sys.stdout.write(result)
            return

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
