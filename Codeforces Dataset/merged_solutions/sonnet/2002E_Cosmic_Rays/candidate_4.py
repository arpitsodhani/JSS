# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def consume_case(items, count):
    st = []
    highest = 0
    out = []
    for _ in range(count):
        amount = next(items)
        number = next(items)
        st.append((number, amount))
        done = False
        while not done:
            done = True
            size = len(st)
            if size >= 2:
                a_value, a_time = st[-2]
                b_value, b_time = st[-1]
                if a_value == b_value:
                    st[-2] = (a_value, a_time + b_time)
                    st.pop()
                    done = False
                    continue
            if len(st) >= 3:
                x_value, x_time = st[-3]
                y_time = st[-2][1]
                z_value, z_time = st[-1]
                if x_value == z_value and y_time < x_time and y_time < z_time:
                    st[-3:] = [(x_value, x_time + z_time - y_time)]
                    done = False
        tail = st[-1][1]
        highest = tail if tail > highest else highest
        out.append(str(highest))
    return " ".join(out)

def main():
    numbers = iter(map(int, sys.stdin.buffer.read().split()))
    t = next(numbers)
    answer = []
    for _ in range(t):
        answer.append(consume_case(numbers, next(numbers)))
    print("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
