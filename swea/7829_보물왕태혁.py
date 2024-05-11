for tc in range(1, int(input())+1):
    p = int(input())
    li = list(map(int, input().split()))
    li.sort()
    print(f'#{tc} {li[0]*li[-1]}')
