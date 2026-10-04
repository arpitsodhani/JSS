# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ServerQueue:
    def __init__(self):
        self.ends = []
        self.first = 0

    def remove_finished(self, moment):
        while self.first < len(self.ends) and self.ends[self.first] <= moment:
            self.first += 1

    def size(self):
        return len(self.ends) - self.first

    def add(self, arrival, duration):
        if self.size() == 0:
            finish = arrival + duration
        else:
            finish = self.ends[-1] + duration
        self.ends.append(finish)
        return finish

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, b = data[:2]
    server = ServerQueue()
    answer = []
    for index in range(2, 2 + 2 * n, 2):
        t = data[index]
        d = data[index + 1]
        server.remove_finished(t)
        if server.size() > b:
            answer.append("-1")
        else:
            answer.append(str(server.add(t, d)))
    sys.stdout.write(" ".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
