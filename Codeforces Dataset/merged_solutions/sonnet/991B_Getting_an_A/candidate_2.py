import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    grades = list(map(int, data[1:n + 1]))
    return n, grades


# --- clause: redo_count :: (n: int, grades: list[int]) -> int ---
def redo_count(n, grades):
    grades.sort()
    total = sum(grades)
    done = 0
    index = 0
    while total * 2 < 9 * n:
        total += 5 - grades[index]
        index += 1
        done += 1
    return done


# --- clause: main :: () -> None ---
def main():
    n, grades = read_input()
    sys.stdout.write("%d\n" % redo_count(n, grades))


if __name__ == "__main__":
    main()
