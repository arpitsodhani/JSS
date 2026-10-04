# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def minimum_changes(columns, query, m):
    current = columns[0].get(query[0], 0)
    if current == 0:
        return -1

    changes = 0
    for index in range(1, m):
        allowed = columns[index].get(query[index], 0)
        if allowed == 0:
            return -1
        kept = current & allowed
        if kept:
            current = kept
        else:
            changes += 1
            current = allowed

    return changes

def main():
    items = sys.stdin.buffer.read().split()
    pos = 0
    n = int(items[pos])
    m = int(items[pos + 1])
    q = int(items[pos + 2])
    pos += 3

    columns = [dict() for _ in range(m)]

    for row in range(n):
        text = items[pos]
        pos += 1
        row_bit = 1 << row
        for col in range(m):
            ch = text[col]
            bucket = columns[col]
            bucket[ch] = bucket.get(ch, 0) | row_bit

    answers = []
    for _ in range(q):
        text = items[pos]
        pos += 1
        answers.append(str(minimum_changes(columns, text, m)))

    sys.stdout.write("\n".join(answers))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
