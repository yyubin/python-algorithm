import sys
n, m, k = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline()) for _ in range(n)]

def check_board(color):
    d = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                tmp = 1 if board[i][j] != color else 0
            else:
                tmp = 1 if board[i][j] == color else 0

            d[i+1][j+1] = d[i+1][j] + d[i][j+1] - d[i][j] + tmp

    count = int(1e9)

    for i in range(n-k+1):
        for j in range(m-k+1):
            repaint = d[i+k][j+k] - d[i][j+k] - d[i+k][j] + d[i][j]
            count = min(count, repaint)

    return count


res = min(check_board("B"), check_board("W"))
print(res)

# 시간복잡도
# O(N*M) -> 누적합계산
# O(K*K) -> 최소값계산
# 정확히는 O(N*M) + O((N-K+1) * (M-K+1))
# K는 N이나 M보다 훨씬 작으므로 무시 가능
# O(N*M)

# 브루트포스로 계산시 N, M이 최대 2000
# N*M을 K^2만큼 계산해야함
# K는 min(N, M)이므로 최악의 경우 N^3나 M^3까지도 가능
# 2000^3은 80억 절대안됨

# 누적 합 계산
# 2차원 배열 누적 합에서는 d[i+1][j+1] + d[i][j+1] + d[i+1][j] - d[i][j] + tmp로 계산가능
# tmp는 현재 고쳐야하는지 아닌지 1로표현함
# i+j % 2가 짝수일 경우 해당 color와 같아야하고 홀수면 달라야함
# 1 더해지는건 현재 잘못칠해진것

# 누적합 모두 계산하고
# n-k+1 , m-k+1 총 k만큼 보드 잘라서 검사
# d[i+k][j+k]는 (0,0)부터 잘못칠해진 개수를 세는 것
# d[i][j+k]랑 d[i+k][j] 부분을 빼주고 두번 빼준 d[i][j]는 다시 더해줌
# 이중에서 가장 작은 값이 답
# w 보드와 b 보드 중 더 작은 것 출력
