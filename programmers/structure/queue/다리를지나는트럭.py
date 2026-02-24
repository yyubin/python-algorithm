from collections import deque

def solution(bridge_length, weight, truck_weights):
    now = 0
    time = 0
    q = deque()
    while True:
        time += 1
        if not q:
            t = truck_weights.pop(0)
            now += t
            q.append((t, time))
            continue

        if time - q[0][1] == bridge_length:
            x = q.popleft()
            now -= x[0]

        if not q and not truck_weights:
            break

        if truck_weights and now + truck_weights[0] <= weight:
            t = truck_weights.pop(0)
            now += t
            q.append((t, time))
    return time


print(solution(2, 10,  	[7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))