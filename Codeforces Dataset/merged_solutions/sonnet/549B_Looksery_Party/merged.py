import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lists = [data[1 + i] for i in range(n)]
    guess = [int(token) for token in data[1 + n:1 + 2 * n]]
    return n, lists, guess

# Clause pick_guests [Confidence: 1.00]
def pick_guests(n, lists, guess):
    need = list(guess)
    coming = []
    invited = [False] * n
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if invited[i] or need[i] != 0:
                continue
            invited[i] = True
            coming.append(i + 1)
            row = lists[i]
            for j in range(n):
                if row[j] == 49:
                    need[j] -= 1
            changed = True
            break
    return coming

# Clause main [Confidence: 1.00]
def main():
    n, lists, guess = read_input()
    coming = pick_guests(n, lists, guess)
    sys.stdout.write(str(len(coming)) + "\n" + " ".join(map(str, coming)) + "\n")


if __name__ == "__main__":
    main()

