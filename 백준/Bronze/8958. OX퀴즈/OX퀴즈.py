for _ in range(int(input())):
    score = streak = 0
    for ch in input().strip():
        streak = streak + 1 if ch == 'O' else 0
        score += streak
    print(score)