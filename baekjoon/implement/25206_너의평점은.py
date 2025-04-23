import sys
li = []
all_grade = 0
score_map = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
all_score = 0
for _ in range(20):
    sub, grade, score = map(str, sys.stdin.readline().split())
    if score != 'P':
        all_grade += float(grade)
        all_score += score_map[score] * float(grade)
print(all_score/all_grade)