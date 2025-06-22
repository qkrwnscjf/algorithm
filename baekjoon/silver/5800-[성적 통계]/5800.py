n = int(input())

for class_num in range(1, n + 1):
    grade = list(map(int, input().split()))
    scores = grade[1:]

    max_score = scores[0]
    min_score = scores[0]
    for s in scores:
        if s > max_score:
            max_score = s
        if s < min_score:
            min_score = s

    # 정렬은 gap 계산용 한 번만 수행
    scores.sort()
    max_gap = 0
    for j in range(len(scores) - 1):
        gap = scores[j + 1] - scores[j]
        if gap > max_gap:
            max_gap = gap

    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {max_gap}")
