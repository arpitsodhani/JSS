# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        if not data:
            return
        n = int(data[0])
        s = data[1]

        balance = 0
        min_balance = 0

        for ch in s:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            min_balance = min(min_balance, balance)

        print("Yes" if balance == 0 and min_balance >= -1 else "No")

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
