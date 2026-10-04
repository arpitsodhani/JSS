def solve():
    n, m = map(int, input().split())
    exams = []
    for i in range(m):
        s, d, c = map(int, input().split())
        exams.append((s, d, c, i + 1))  # start, exam_day, prep_needed, exam_id
    
    # Sort by exam day (earlier exams first)
    exams.sort(key=lambda x: x[1])
    
    schedule = [0] * (n + 1)  # schedule[day] = exam being worked on (0 = rest)
    prep_done = [0] * (m + 1)  # prep_done[exam_id] = days of prep completed
    
    # Mark exam days and check for conflicts
    for s, d, c, exam_id in exams:
        if schedule[d] != 0:
            print(-1)
            return
        schedule[d] = exam_id
    
    # Assign preparation days greedily
    for day in range(1, n + 1):
        if schedule[day] != 0:  # Day already assigned (exam day)
            continue
        
        # Find exam with earliest deadline that needs prep and can be prepped today
        best_exam = None
        for s, d, c, exam_id in exams:
            if s <= day < d and prep_done[exam_id] < c:
                best_exam = exam_id
                break  # First valid exam has earliest deadline (sorted)
        
        if best_exam is not None:
            schedule[day] = best_exam
            prep_done[best_exam] += 1
    
    # Verify all exams have enough preparation
    for s, d, c, exam_id in exams:
        if prep_done[exam_id] < c:
            print(-1)
            return
    
    print(' '.join(map(str, schedule[1:])))

solve()
