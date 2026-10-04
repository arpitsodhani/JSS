# CLAUSE: setup_environment
import sys

def build_tables(arr):
    ranked = sorted(enumerate(arr), key=lambda x: (-x[1], x[0]))
    tables = [[] for _ in range(len(arr) + 1)]
    picked = [False] * len(arr)
    for size, (index, value) in enumerate(ranked, 1):
        picked[index] = True
        current = []
        for i, selected in enumerate(picked):
            if selected:
                current.append(arr[i])
        tables[size] = current
    return tables

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    n = int(tokens[0])
    arr = [int(x) for x in tokens[1:1 + n]]
    tables = build_tables(arr)
    qpos = 1 + n
    q = int(tokens[qpos])
    qpos += 1
    answers = []
    for i in range(q):
        k = int(tokens[qpos + 2 * i])
        place = int(tokens[qpos + 2 * i + 1])
        answers.append(str(tables[k][place - 1]))

# CLAUSE: finish_program
    print("\n".join(answers))

if __name__ == "__main__":
    main()
