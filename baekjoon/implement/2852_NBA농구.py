import sys

def time_to_sec(time_str):
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def sec_to_time(sec):
    m = sec // 60
    s = sec % 60
    return f"{m:02d}:{s:02d}"

n = int(sys.stdin.readline())
score = [0, 0]
win_time = [0, 0]

prev_time = 0
leader = 0

for _ in range(n):
    team_str, time_str = sys.stdin.readline().split()
    team = int(team_str) - 1
    curr_time = time_to_sec(time_str)

    if score[0] != score[1]:
        win_time[leader] += curr_time - prev_time
    score[team] += 1

    if score[0] > score[1]:
        leader = 0
    elif score[0] < score[1]:
        leader = 1
    else:
        leader = -1

    prev_time = curr_time

if score[0] != score[1]:
    win_time[leader] += (48 * 60) - prev_time

print(sec_to_time(win_time[0]))
print(sec_to_time(win_time[1]))
