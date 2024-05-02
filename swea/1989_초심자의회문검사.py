for tc in range(int(input())):
    li = list(input())
    print(f"#{tc+1} {1 if li == li[::-1] else 0}")
