# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys

    def main():
        data = list(map(int, sys.stdin.buffer.read().split()))
        n = data[0]
        a = data[1:]
        h = n // 2

        div = [i for i, x in enumerate(a) if x % 3 == 0]
        non = [i for i, x in enumerate(a) if x % 3 != 0]

        s = ['1'] * n

        if len(div) <= h:
            z = 0
            for i in div:
                s[i] = '0'
            need = h - len(div)
            for i in non[:need]:
                s[i] = '0'
        else:
            z = 2
            for i in non:
                s[i] = '0'
            need = h - len(non)
            for i in div[:need]:
                s[i] = '0'

        print(z)
        print(''.join(s))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
