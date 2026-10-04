# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def attempt(root, indexed, n):
    labels = [""] * (2 * n - 2)
    for length in range(1, n):
        current = indexed[length]
        prefix = root[:length]
        suffix = root[-length:]

        matched = False
        for first_label, second_label in (("P", "S"), ("S", "P")):
            first_text = prefix if first_label == "P" else suffix
            second_text = prefix if second_label == "P" else suffix
            if current[0][1] == first_text and current[1][1] == second_text:
                labels[current[0][0]] = first_label
                labels[current[1][0]] = second_label
                matched = True
                break

        if not matched:
            return None

    return "".join(labels)

def main():
    raw = sys.stdin.buffer.read().split()
    n = int(raw[0])
    strings = [part.decode() for part in raw[1:]]
    indexed = [[] for _ in range(n)]

    for index in range(len(strings)):
        indexed[len(strings[index])].append((index, strings[index]))

    top = indexed[-1]
    candidates = []
    candidates.append(top[0][1] + top[1][1][-1])
    candidates.append(top[1][1] + top[0][1][-1])

    answer = attempt(candidates[0], indexed, n)
    if answer is None:
        answer = attempt(candidates[1], indexed, n)
    sys.stdout.write(answer)

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
