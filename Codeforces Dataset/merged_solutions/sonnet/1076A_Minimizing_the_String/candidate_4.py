# CLAUSE: setup_environment
n = int(input())
s = input().strip()

# CLAUSE: solve_logic
def removal_position(text):
    for pos, pair in enumerate(zip(text, text[1:])):
        if pair[0] > pair[1]:
            return pos
    return len(text) - 1

cut = removal_position(s)
answer = "".join(s[i] for i in range(n) if i != cut)

# CLAUSE: finish_program
print(answer)
