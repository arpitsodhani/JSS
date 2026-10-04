# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def winner(entries):
    final = {}
    for name, delta in entries:
        final[name] = final.get(name, 0) + delta

    highest = None
    for value in final.values():
        if highest is None or value > highest:
            highest = value

    eligible = {}
    for name, value in final.items():
        if value == highest:
            eligible[name] = True

    seen = {}
    for name, delta in entries:
        seen[name] = seen.get(name, 0) + delta
        if eligible.get(name, False) and seen[name] >= highest:
            return name

def main():
    tokens = sys.stdin.buffer.read().split()
    count = int(tokens[0])
    entries = []
    index = 1

    while count:
        entries.append((tokens[index].decode(), int(tokens[index + 1])))
        index += 2
        count -= 1

    sys.stdout.write(winner(entries))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
