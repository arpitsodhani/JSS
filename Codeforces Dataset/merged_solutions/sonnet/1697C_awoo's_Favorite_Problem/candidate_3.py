# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def check(n, s, t):
    i = 0
    j = 0
    while i < n or j < n:
        while i < n and s[i] == "b":
            i += 1
        while j < n and t[j] == "b":
            j += 1
        if i == n or j == n:
            return i == n and j == n
        if s[i] != t[j]:
            return False
        if s[i] == "a" and i > j:
            return False
        if s[i] == "c" and i < j:
            return False
        i += 1
        j += 1
    return True

# CLAUSE: finish_program
def main():
    tokens = sys.stdin.buffer.read().split()
    q = int(tokens[0])
    answers = []
    at = 1
    for _ in range(q):
        n = int(tokens[at])
        s = tokens[at + 1].decode()
        t = tokens[at + 2].decode()
        at += 3
        answers.append("YES" if check(n, s, t) else "NO")
    print("\n".join(answers))

if __name__ == "__main__":
    main()
