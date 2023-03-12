import sys
sys.setrecursionlimit(10**6)

li = []
while True:
    try:
        num = int(sys.stdin.readline())
        li.append(num)
    except:
        break

def dfs(left, right): #0, 8
    if left > right:
        return
    else:
        mid = right + 1 # mid = 9
        for i in range(left+1, right+1): # 1 ~ 9
            if li[left] < li[i]: #li[0] < li[i]
                mid = i          #mid = i #45 #5
                break
        dfs(left+1, mid-1)       #1, 4
        dfs(mid, right)          #5, 8
        print(li[left])
        # 원소가 현재 노드보다 클 경우 그전까지는 왼쪽 그 이후는 오른쪽
dfs(0, len(li)-1)

## dfs인지 생각을 못함..ㅠㅠㅠ