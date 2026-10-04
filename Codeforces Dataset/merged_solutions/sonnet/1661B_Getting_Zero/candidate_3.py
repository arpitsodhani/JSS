# CLAUSE: setup_environment
import sys

LIMIT = 32768

# CLAUSE: solve_logic
def best_steps(x):
    answer = 20
    add = 0
    while add <= 15:
        value = (x + add) % LIMIT
        times = 0
        while times <= 15:
            if (value << times) % LIMIT == 0:
                cost = add + times
                if cost < answer:
                    answer = cost
                break
            times += 1
        add += 1
    return answer

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    result = []
    for number in data[1:n + 1]:
        result.append(str(best_steps(number)))
    print(" ".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
