for tc in range(int(input())):
    li = list(map(int, input().split()))
    li.sort()
    li.pop(0)
    li.pop()
    print(f'#{tc+1} {round(sum(li)/len(li))}')
