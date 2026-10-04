n, m = map(int, input().split())
correct = list(map(int, input().split()))
wrong = list(map(int, input().split()))

max_correct = max(correct)
min_correct = min(correct)
min_wrong = min(wrong)

v = max(max_correct, 2 * min_correct)

if v < min_wrong:
    print(v)
else:
    print(-1)
