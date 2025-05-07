import sys
def toggle(state, idx):
    for i in [idx-1, idx, idx+1]:
        if 0 <= i < len(state):
            state[i] = '1' if state[i] == '0' else '0'

def simulate(start, target, press_first):
    state = list(start)
    cnt = 0
    if press_first:
        toggle(state, 0)
        cnt += 1
    for i in range(1, len(state)):
        if state[i-1] != target[i-1]:
            toggle(state, i)
            cnt += 1

    return cnt if state == list(target) else sys.maxsize

n = int(sys.stdin.readline())
start = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

res1 = simulate(start, target, True)
res2 = simulate(start, target, False)
res = min(res1, res2)
print(res if res < sys.maxsize else -1)

# 앞에서부터 i-1번 전구를 기준으로 고친다 (그리디)
# 1번 스위치를 누른/안 누른 두 시나리오로 분기
# 최종 상태가 맞는지 확인해서 최소 클릭 수를 구함

# i-1번째 전구를 목표 상태와 같게 만드는 유일한 방법은 i번 스위치를 누르는 것뿐
# 앞에서부터 진행하면서 결정해야지, 뒤에서 고치려고 하면 이미 고친 전구가 또 바뀔 수 있어 백트래킹이 필요해짐 → 비효율적